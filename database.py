import psycopg2
from psycopg2 import OperationalError
import os
from dotenv import load_dotenv
import pandas as pd
import time
from datetime import datetime
from utils import limite_date

load_dotenv()

def connect_to_db():
    while True:
        try:
            db = psycopg2.connect(
                host="db",
                port=5432,
                dbname=os.getenv("POSTGRES_DB"),
                user=os.getenv("POSTGRES_USER"),
                password=os.getenv("POSTGRES_PASSWORD")
            )
            return db
        except OperationalError as e:
            print("Database not ready yet, retrying...")
            time.sleep(5)


def get_data_from_db(date):
    db_connect = connect_to_db()
    cur = db_connect.cursor()

    date_str = str(date)
    date_formatted = datetime.strptime(date_str, '%Y%m%d').strftime('%Y-%m-%d')

    try:
        cur.execute(
            "SELECT date, stat FROM stats WHERE date >= %s AND date <= %s "
            "ORDER BY date;", (limite_date(), date_formatted))
        data = cur.fetchall()
        df = pd.DataFrame(data, columns=['date', 'stat'])
        return df[['date', 'stat']].rename(columns={'date': 'ds', 'stat': 'y'})
    except psycopg2.Error as err:
        print(f"Error: {err}")
    finally:
        cur.close()

def add_data_to_db(stat_to_add):
    date = datetime.today().strftime('%Y-%m-%d')
    db_connect = connect_to_db()
    cur = db_connect.cursor()
    try:
        cur.execute("INSERT INTO stats (date, stat) VALUES (%s, %s)", (date, stat_to_add))
        db_connect.commit()
    except psycopg2.Error as err:
        print(f"Error: {err}")
    finally:
        cur.close()
