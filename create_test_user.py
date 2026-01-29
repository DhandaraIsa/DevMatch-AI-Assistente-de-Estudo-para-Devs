import sys
import os
import hashlib
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

# Cria hash de senha simples (SHA256)
password_hash = hashlib.sha256("12345".encode()).hexdigest()

# Cria usuário de teste
test_user = User(
    name="Test User",
    email="test@devmatch.ai",
    password_hash=password_hash
)

try:
    # Verifica se usuário já existe
    existing = db.query(User).filter(User.email == "test@devmatch.ai").first()
    if existing:
        print("✓ Usuário de teste já existe")
    else:
        db.add(test_user)
        db.commit()
        print("✓ Usuário de teste criado!")
        print(f"  Email: test@devmatch.ai")
        print(f"  Senha: 12345")
except Exception as e:
    print(f"✗ Erro: {e}")
finally:
    db.close()
