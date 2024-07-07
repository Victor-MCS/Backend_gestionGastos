from app.utils.db import get_db_connection

class UsuarioRepository:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM public."Usuario"')
        usuarios = cursor.fetchall()
        cursor.close()
        conn.close()
        return usuarios

    @staticmethod
    def get_by_id(id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM public."Usuario" WHERE "idUser" = %s;', (id,))
        usuarios = cursor.fetchone()
        cursor.close()
        conn.close()
        return usuarios

    @staticmethod
    def create(data):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO registros (campo1, campo2) VALUES (%s, %s) RETURNING id;',
            (data['campo1'], data['campo2'])
        )
        usuarios_id = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        conn.close()
        return {'id': usuarios_id, **data}

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
