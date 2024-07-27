import psycopg2
from sqlalchemy import create_engine, Column, Integer, String
from dotenv import load_dotenv
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создаем подключение к базе данных
load_dotenv()

DB_CONFIG = {
    'dbname': os.environ.get("DB_NAME"),
    'host': os.environ.get("HOST"),
    'user': os.environ.get("USER"),
    'port': os.environ.get("PORT"),
    'password': os.environ.get("PASSWORD")
}
def db_connection():
    return psycopg2.connect(**DB_CONFIG)

# Создаем движок для работы с базой данных
engine = create_engine('postgresql://postgres:Junior(23)@localhost/postgres')




