import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv

load_dotenv()

from sqlalchemy import create_engine
from database import Base
import models

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL not set in environment")

engine = create_engine(DATABASE_URL)

def main():
    print(f"Creating tables using DATABASE_URL={DATABASE_URL}")
    Base.metadata.create_all(bind=engine)
    print("Tables created (if not existing).")

if __name__ == '__main__':
    main()
