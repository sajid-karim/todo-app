from sqlalchemy import Column, Integer, String, Boolean
from database.engine import Base


class Token(Base):
  __tablename__ = "tokens"

  id = Column(Integer, primary_key=True, index=True)
  token = Column(String, index=True)
  user_id = Column(Integer, index=True)
  is_active = Column(Boolean, default=True)
