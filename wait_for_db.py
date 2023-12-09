import psycopg2
from environs import Env
import time

env = Env()
env.read_env()

db_params = {
    'dbname': env('POSTGRES_DB'),
    'user': env('POSTGRES_USER'),
    'password': env('POSTGRES_PASSWORD'),
    'host': env('POSTGRES_HOST'),
    'port': env("POSTGRES_PORT"),
}

max_retries = 30
retries = 0

while retries < max_retries:
    try:
        conn = psycopg2.connect(**db_params)
        conn.close()
        print("Database is ready.")
        break
    except psycopg2.OperationalError:
        print("Waiting for the database...")
        time.sleep(2)
        retries += 1
