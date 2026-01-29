from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(120), nullable=False)
    email = Column(String(200), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)

    items = relationship("StudyItem", back_populates="user")

class StudyItem(Base):
    __tablename__ = "study_items"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    kind = Column(String(30), nullable=False)  # plan | questions | explain
    topic = Column(String(120), nullable=False)
    level = Column(String(30), nullable=False) # beginner | medium | advanced
    content = Column(Text, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="items")
