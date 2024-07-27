from database import db_connection, DB_CONFIG
import os
from dotenv import load_dotenv
import psycopg2




def get_unique_values(column_name):
    with db_connection() as connection:
        query = f'SELECT DISTINCT "{column_name}" FROM voters'
        with connection.cursor() as cursor:
            cursor.execute(query)
            unique_values = cursor.fetchall()
            return [value[0] for value in unique_values]

def split_array(arr):
    new_arr = []
    for i in range(0, len(arr), 4):
        new_arr.append(arr[i:i+4])
    return new_arr

def get_values_by_year_and_states(year1, states):
    with db_connection() as connection:
        states_str = ','.join([f"'{state}'" for state in states])
        query = f'SELECT quantity FROM voters WHERE "Year" = {year1} AND "Jurisdiction" IN ({states_str})'
        with connection.cursor() as cursor:
            cursor.execute(query)
            values = cursor.fetchall()
        votes = [value[0] for value in values]
        return split_array(votes)


