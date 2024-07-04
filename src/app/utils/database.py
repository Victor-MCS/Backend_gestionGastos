import psycopg2
from psycopg2 import sql

def init_db():
    try:
        conn = psycopg2.connect(
            dbname="fake_db",
            user="fake_user",
            password="fake_password",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute(sql.SQL("""
            CREATE TABLE IF NOT EXISTS expenses (
                id SERIAL PRIMARY KEY,
                description TEXT NOT NULL,
                amount DECIMAL NOT NULL,
                date DATE NOT NULL
            );
        """))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error initializing database: {e}")
