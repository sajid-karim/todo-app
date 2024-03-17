import os
import dotenv

if os.path.isfile('.env.local'):
    dotenv.load_dotenv(dotenv_path='.env.local')
    
def get_env_vars():
  db_host = os.getenv("DB_HOST")
  db_port = os.getenv("DB_PORT")
  db_name = os.getenv("DB_NAME")
  db_user = os.getenv("DB_USER")
  db_password = os.getenv("DB_PASSWORD")

  if not all([db_host, db_port, db_name, db_user, db_password]):
    raise ValueError("Missing required database environment variables")

  return db_host, db_port, db_name, db_user, db_password




# Load environment variables
db_host, db_port, db_name, db_user, db_password = get_env_vars()