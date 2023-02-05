import os
from dotenv import load_dotenv
from sqlalchemy import create_engine


def create_postgres_engine():
    load_dotenv()
    user = os.getenv('POSTGRES_USER')
    pwd = os.getenv('POSTGRES_PWD')
    hostname = os.getenv('POSTGRES_HOSTNAME')
    db = os.getenv('POSTGRES_DB')

    return create_engine(f'postgresql+psycopg2://{user}:{pwd}@{hostname}/{db}')
