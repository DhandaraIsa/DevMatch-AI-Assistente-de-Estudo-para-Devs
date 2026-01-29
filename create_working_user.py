import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), r"backend"))

from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"backend\app\.env"))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import User
from app.auth import hash_password

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

db = SessionLocal()

try:
    test_user = User(
        name="Test User",
        email="test@devmatch.ai",
        password_hash=hash_password("12345")
    )
    
    db.add(test_user)
    db.commit()
    print("✓ Usuário de teste criado com sucesso!")
    print(f"  Email: test@devmatch.ai")
    print(f"  Senha: 12345")
    print(f"  Hash: {test_user.password_hash[:40]}...")
    
except Exception as e:
    print(f"✗ Erro: {e}")
    import traceback
    traceback.print_exc()
finally:
    db.close()
