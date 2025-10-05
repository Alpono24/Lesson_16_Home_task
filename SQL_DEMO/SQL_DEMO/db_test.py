import os
from sqlalchemy import create_engine, text


DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:postgres@localhost:5432/library_db")
engine = create_engine(DATABASE_URL, echo=False)
with engine.connect() as conn:
    print("connected:", conn.execute(text("SELECT 1;")).scalar())



