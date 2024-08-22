from typing import ClassVar
from pydantic_settings import BaseSettings
from sqlalchemy.orm import declarative_base

class Settings(BaseSettings):

    API_V1_STR: str = '/api/v1'
    DSNNAME: str = 'FavMovie'
    DB_URL: str = f'mssql+aioodbc://CA-C-004Y3\SQLEXPRESS/{DSNNAME}?driver=ODBC+Driver+17+for+SQL+Server&TrustServerCertificate=yes'
    
    DBBaseModel: ClassVar = declarative_base()

    # DB_URL: ClassVar = URL.create(
    #     "mssql+aioodbc",
    #     username=USERNAME,
    #     password=PASSWORD,
    #     database=DSNNAME,  # required; not an empty string
    #     query={"driver": 'ODBC Driver 17 for SQL Server'}
    # )

    class Config:
        case_sensitive = False
        env_file = '../venv'

settings = Settings()