import pydantic
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
# class Settings(BaseSettings):
#     DB_HOST: str = 'localhost'  # Теперь это типизированное поле
#     DB_PORT: int = 5432
#     DB_USER: str = 'postgres'
#     DB_PASS: str = 'password'
#     DB_NAME: str = 'DB_SHUM'

# @property
# def DATABASE_URL_asyncpg(self):
#     # postgresql+asyncpg://postgres:postgres@localhost:5432/DB_SHUM
#     return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

@property
def DATABASE_URL_psycopg(self):
    #DSN
    # postgresql+psycopg://postgres:postgres@localhost:5432/DB_SHUM
    # "postgresql+psycopg2://postgres:postgres@localhost:5432/DB_SHUM"
    return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


model_config = SettingsConfigDict(env_file='../.env', extra='ignore')

settings = Settings()


