from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.engine import Base
from models.todo import TodoItem

class User(Base):
  __tablename__ = "users"
  
  id = Column(Integer, primary_key=True, index=True)
  username = Column(String, unique=True, index=True)
  email = Column(String, unique=True, index=True)
  password = Column(String)
  todos = relationship("TodoItem", back_populates="owner")
  
  def __repr__(self):
    return f"<User(id={self.id}, username={self.username}, email={self.email})>"
  
  def __str__(self):
    return f"<User(id={self.id}, username={self.username}, email={self.email})>"