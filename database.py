import psycopg2
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создаем подключение к базе данных
connection = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="Junior(23)",
    host="localhost",
)

# Создаем движок для работы с базой данных
engine = create_engine('postgresql://postgres:Junior(23)@localhost/postgres')




