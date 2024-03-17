from sqlalchemy import Column, Integer, String, Boolean, ForeignKey 
from sqlalchemy.orm import relationship
from database.engine import Base


class  TodoItem(Base):
  __tablename__ = "todos"

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, index=True)
  description = Column(String, index=True)
  completed = Column(Boolean, default=False)
  
  owner_id = Column(Integer, ForeignKey("users.id"))
  owner = relationship("User", back_populates="todos")
  