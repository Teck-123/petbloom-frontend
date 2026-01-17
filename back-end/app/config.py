from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/petbloom"
    FBASE_CREDENTIALS: str = "path/to/fbase-credentials.json"
    JWT_SECRET: str = "your-super-secret-jwt-key"
    JWT_ALGORITHM: str = "HS256"
    API_URL: str = "http://localhost:8000"
    FRONTEND_URL: str = "http://localhost:5173"

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()
