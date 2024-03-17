from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import models
from configs import db_host, db_port, db_name, db_user, db_password


# Define the engine class 
class Engine:
  def __init__(self):
    self.engine = create_engine(
      f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    )
    self.SessionLocal = sessionmaker(bind=self.engine)
    
    self.Base = declarative_base()

  def get_engine(self):
    return self.engine
  
  def session(self):
    return self.SessionLocal
  
  def get_session(self):
    db = self.SessionLocal()
    try:
      yield db
    finally:
      db.close()
      
  def base(self):
    return self.Base
  

# Define the engine instance
DBengine = Engine()
# Define the base instance
Base = DBengine.base()

  

  
