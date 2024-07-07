from app.utils.db import get_db_connection

class TarjetasRepository:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM public."Tarjeta"')
        tarjetas = cursor.fetchall()
        cursor.close()
        conn.close()
        return tarjetas

    @staticmethod
    def get_by_id(id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM public."Tarjeta" WHERE "idTarjeta" = %s;', (id,))
        tarjetas = cursor.fetchone()
        cursor.close()
        conn.close()
        return tarjetas

    @staticmethod
    def create(data):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO registros (campo1, campo2) VALUES (%s, %s) RETURNING id;',
            (data['campo1'], data['campo2'])
        )
        tarjetas_id = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        conn.close()
        return {'id': tarjetas_id, **data}

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
