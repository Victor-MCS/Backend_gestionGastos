from app.utils.db import get_db_connection

class AuthRepository:
    @staticmethod
    def create_user(email, name, password):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO public."Usuario" (email, name, password) VALUES (%s, %s, %s);', (email, name, password))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_user(email, password):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM public."Usuario" WHERE email = %s and password = %s;', (email,password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user
