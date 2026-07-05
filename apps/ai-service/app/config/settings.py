from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    APP_NAME: str = "SwasthAI AI Service"
    APP_VERSION: str = "1.0.0"
    API_PREFIX: str = "/api/v1"

    DEBUG: bool = True

    HOST: str = "0.0.0.0"
    PORT: int = 8000

    MONGODB_URI: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "swasthai"

    CHROMA_DB_PATH: str = "./rag/vectordb"

    EMBEDDING_MODEL: str = "BAAI/bge-small-en-v1.5"
    LLM_MODEL: str = "llama3"

    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()