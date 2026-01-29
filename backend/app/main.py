from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from .models import User, StudyItem
from .schemas import (
    UserCreate, UserLogin, TokenOut,
    AIPlanIn, AIQuestionsIn, AIExplainIn,
    StudyItemOut
)
from .auth import hash_password, verify_password, create_access_token, get_current_user
from .ai import gemini_generate, prompt_plan, prompt_questions, prompt_explain

app = FastAPI(title="DevMatch AI API", version="1.0.0")

@app.on_event("startup")
def create_tables():
    Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

# ---------- Auth ----------
@app.post("/auth/register", response_model=TokenOut)
def register(payload: UserCreate, db: Session = Depends(get_db)):
    exists = db.query(User).filter(User.email == payload.email).first()
    if exists:
        raise HTTPException(400, "E-mail já cadastrado.")

    user = User(
        name=payload.name,
        email=payload.email,
        password_hash=hash_password(payload.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token}

@app.post("/auth/login", response_model=TokenOut)
def login(payload: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()
    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(401, "Credenciais inválidas.")

    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token}

# ---------- AI ----------
@app.post("/ai/plan", response_model=StudyItemOut)
async def ai_plan(payload: AIPlanIn, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    text = await gemini_generate(prompt_plan(payload.topic, payload.level))
    item = StudyItem(user_id=user.id, kind="plan", topic=payload.topic, level=payload.level, content=text)
    db.add(item); db.commit(); db.refresh(item)
    return item

@app.post("/ai/questions", response_model=StudyItemOut)
async def ai_questions(payload: AIQuestionsIn, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    text = await gemini_generate(prompt_questions(payload.topic, payload.level))
    item = StudyItem(user_id=user.id, kind="questions", topic=payload.topic, level=payload.level, content=text)
    db.add(item); db.commit(); db.refresh(item)
    return item

@app.post("/ai/explain", response_model=StudyItemOut)
async def ai_explain(payload: AIExplainIn, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    text = await gemini_generate(prompt_explain(payload.topic, payload.level, payload.error_text))
    item = StudyItem(user_id=user.id, kind="explain", topic=payload.topic, level=payload.level, content=text)
    db.add(item); db.commit(); db.refresh(item)
    return item

# ---------- History ----------
@app.get("/history", response_model=list[StudyItemOut])
def history(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return (
        db.query(StudyItem)
        .filter(StudyItem.user_id == user.id)
        .order_by(StudyItem.created_at.desc())
        .all()
    )
