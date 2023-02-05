import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

_user = os.getenv('POSTGRES_USER')
_password = os.getenv('POSTGRES_PWD')
_hostname = os.getenv('POSTGRES_HOSTNAME')
_database = os.getenv('POSTGRES_DB')

engine = create_engine(
    f'postgresql+psycopg2://{_user}:{_password}@{_hostname}/{_database}')

Session = sessionmaker(engine)
