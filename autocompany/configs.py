import os

from dotenv import load_dotenv

load_dotenv()
LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG')
POSTGRES_DB_NAME = os.environ.get('NAME')
POSTGRES_USER_NAME = os.environ.get('POSTGRES_USER_NAME')
POSTGRES_PASSWORD = os.environ.get('PASSWORD')
POSTGRES_HOST = os.environ.get('HOST')
POSTGRES_PORT = os.environ.get('PORT')
