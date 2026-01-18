from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import Optional

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:vtdBjkgxHkBPDdFYnlvmSCcPbklgEicd@postgres.railway.internal:5432/railway"
    FBASE_CREDENTIALS: Optional[str] = None
    JWT_SECRET: str = "test-secret-key-change-in-production"
    JWT_ALGORITHM: str = "HS256"
    API_URL: str = "http://localhost:8000"
    FRONTEND_URL: str = "https://pet-bloom.vercel.app"
    ENVIRONMENT: str = "development"

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()
