import os
from sqlalchemy import create_engine, text

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:postgres@localhost:5432/DB_SHUM")


engine = create_engine(
    url=DATABASE_URL,
    echo=False
    # pool_size=5,
    # max_overflow=10
)

with engine.connect() as conn:
    # result = conn.execute(text('SELECT VERSION()')).fetchall()
    # print(result)
    # conn.commit()
    print("connected:", conn.execute(text("SELECT 1;")).scalar())

# if __name__ == "__main__":
#     print("Database URL:", settings.DATABASE_URL_psycopg)


