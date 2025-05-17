from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL = "postgresql+psycopg2://postgres:postgres_password@postgres:5432/price_data"

engine = create_engine(DB_URL)
local_session = sessionmaker(autocommit = False, autoflush=False, bind=engine)

def get_db_session():
    db = local_session()
    try:
        yield db
    finally:
        db.close()