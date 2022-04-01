from pydantic import BaseSettings


class Settings(BaseSettings):
    REMOTE_USERS_API: str

    class Config:
        env_file = ".env"


settings = Settings()
