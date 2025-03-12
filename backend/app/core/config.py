import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DB_NAME: str = os.getenv("DB_NAME", "trueque_db")
    DB_USER: str = os.getenv("DB_USER", "trueque_user")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "trueque_pass")
    DB_HOST: str = os.getenv("DB_HOST", "db")
    DB_PORT: str = os.getenv("DB_PORT", "5432")

    DATABASE_URL: str = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

settings = Settings()
