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

try:
    # Remove todos os usuários
    db.query(User).delete()
    db.commit()
    print("✓ Banco limpo")
except Exception as e:
    print(f"✗ Erro: {e}")
finally:
    db.close()
