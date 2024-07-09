from app.utils.db import get_db_connection
import json

class UsuarioRepository:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT email, name, password FROM public."Usuario"')
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        usuarios = [{'email': row[0], 'name': row[1], 'password': row[2]} for row in rows]
        return json.dumps(usuarios)  

    @staticmethod
    def get_by_id(id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT email, name, password FROM public."Usuario" WHERE "idUser" = %s;', (id,))
        usuarios = cursor.fetchone()
        if usuarios == None:
            return usuarios
        cursor.close()
        conn.close()
        usuarios = {'email':usuarios[0], 'name': usuarios[1], 'password': usuarios[2]}
        return usuarios


    # Metodo para validar si el email existe
    @staticmethod
    def email_exists(email,cursor):
        cursor.execute('SELECT 1 FROM public."Usuario" WHERE email = %s;', (email,))
        exists = cursor.fetchone() is not None
        return exists
    

    @staticmethod
    def create(data):
        conn = get_db_connection()
        cursor = conn.cursor()
        if UsuarioRepository.email_exists(data['email'],cursor):
            return {"error": "El correo ya está registrado"}
        cursor.execute(
            'INSERT INTO public."Usuario" (email, name, password) VALUES (%s, %s, %s);',
            (data['email'], data['name'], data['password'])
        )
        email = data['email']
        conn.commit()
        cursor.close()
        conn.close()
        return {"message": f"El correo {email} ha sido registrado"}

    @staticmethod
    def update(id, data):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE registros SET campo1 = %s, campo2 = %s WHERE id = %s;',
            (data['campo1'], data['campo2'], id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return {'id': id, **data}

    @staticmethod
    def delete(id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM registros WHERE id = %s;', (id,))
        conn.commit()
        cursor.close()
        conn.close()
