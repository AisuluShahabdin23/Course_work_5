import psycopg2
from db_manager import DBManager


def create_db(db_name: str, params: dict):
    """
    Создаёт базу данных и таблицы для сохранения данных
    """
    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f"DROP DATABASE IF EXISTS {db_name}")
    cur.execute(f"CREATE DATABASE {db_name}")

    cur.close()
    conn.close()

    conn = psycopg2.connect(dbname=db_name, **params)

    with conn.cursor() as cur:
        cur.execute("""
                CREATE TABLE employers (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL
                )
            """)

    with conn.cursor() as cur:
        cur.execute("""
                CREATE TABLE vacancies (
                    name VARCHAR(255) NOT NULL,
                    employer VARCHAR NOT NULL,
                    salary INT,
                    employer_id SERIAL REFERENCES employers(id),
                    url TEXT 
                )
            """)
    conn.commit()
    conn.close()


def fill_table_companies(data, db_name: str, params: dict):
    """
    Заполняем таблицу с данными компаний
    """
    conn = psycopg2.connect(dbname=db_name, **params)
    with conn.cursor() as cur:
        for employer in data:
            query = "INSERT INTO employers (id, name) VALUES (%s, %s) ON CONFLICT DO NOTHING"
            cur.execute(query, employer)
    conn.commit()
    conn.close()


def fill_table_vacancies(data, db_name: str, params: dict):
    """
    Заполняем таблицу с вакансиями
    """
    conn = psycopg2.connect(dbname=db_name, **params)
    with conn.cursor() as cur:
        for vacancy in data:
            query = "INSERT INTO vacancies (name, employer, salary, employer_id, url) VALUES (%s, %s, %s, %s, %s)"
            cur.execute(query, vacancy)

    conn.commit()
    conn.close()
