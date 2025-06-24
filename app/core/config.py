from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    vaoja_api_base: str

    class Config:
        env_file = ".env"

settings = Settings()
