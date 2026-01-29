import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), r"backend"))

from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"backend\app\.env"))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.models import User

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

db = SessionLocal()

try:
    # Remove usuário anterior
    existing = db.query(User).filter(User.email == "test@devmatch.ai").first()
    if existing:
        db.delete(existing)
        db.commit()
        print("✓ Usuário antigo removido")
    
    # Cria novo usuário com senha bcrypt pré-computada
    # Hash bcrypt da senha "12345" (gerado externamente)
    bcrypt_hash = "$2b$12$N9qo8uLOickgx2ZMRZoMyeIjZAgcg7b3XeKeUxWdeS86AGR0Ifj.i"
    
    test_user = User(
        name="Test User",
        email="test@devmatch.ai",
        password_hash=bcrypt_hash
    )
    
    db.add(test_user)
    db.commit()
    print("✓ Usuário criado com bcrypt hash!")
    print(f"  Email: test@devmatch.ai")
    print(f"  Senha: 12345")
    
except Exception as e:
    print(f"✗ Erro: {e}")
    import traceback
    traceback.print_exc()
finally:
    db.close()
