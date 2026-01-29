import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), r"backend"))

from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"backend\app\.env"))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import User

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

db = SessionLocal()

# Busca o usuário
user = db.query(User).filter(User.email == "test@devmatch.ai").first()

if user:
    print(f"✓ Usuário encontrado: {user.email}")
    print(f"  Hash armazenado: {user.password_hash}")
    print(f"  Hash length: {len(user.password_hash)}")
else:
    print("✗ Usuário não encontrado")

db.close()
