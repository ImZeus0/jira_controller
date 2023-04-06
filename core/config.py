import os
from pydantic import BaseSettings, AnyHttpUrl
from functools import lru_cache
import os
class Settings(BaseSettings):
    octo_ip:str
    token_octo:str
    git_hub_token:str


    class Config:
        #env_file = os.path.join(os.getcwd(),'core','config.env')
        env_file = '/home/zeus/PycharmProjects/jira_controller/core/config.env'
        env_file_encoding = 'utf-8'


@ lru_cache
def get_settings() -> Settings:
    settings = Settings()

    return settings
