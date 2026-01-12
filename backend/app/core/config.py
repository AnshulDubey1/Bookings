from pydantic_settings import BaseSettings,SettingsConfigDict
from pydantic import (Field)
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
env_path =BASE_DIR/".env"

class Settings(BaseSettings):
    model_config=SettingsConfigDict(env_file=env_path,env_file_encoding='UTF-8')
    redis_host:str=Field(...,alias="REDIS_HOST")
    redis_port:int=Field(...,alias="REDIS_PORT")
    app_name:str=Field(alias="APP_NAME")
    app_version:str=Field(...,alias="APP_VERSION")
    debug:bool=Field(default=False,alias="DEBUG")
    

settings=Settings()