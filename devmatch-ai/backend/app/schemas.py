from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"

class AIPlanIn(BaseModel):
    topic: str
    level: str  # medium etc.

class AIExplainIn(BaseModel):
    topic: str
    level: str
    error_text: str

class AIQuestionsIn(BaseModel):
    topic: str
    level: str

class StudyItemOut(BaseModel):
    id: int
    kind: str
    topic: str
    level: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True
