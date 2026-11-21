from pydantic import AliasChoices, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    database_hostname: str
    database_port: str
    database_password: str 
    database_name:str
    database_username:str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int = Field(
        validation_alias=AliasChoices("ACCESS_TOKEN_EXPIRE_MINUTES", "ACCESS_TOKEN_EXPIRE_MINUTE")
    )

settings=Settings()
