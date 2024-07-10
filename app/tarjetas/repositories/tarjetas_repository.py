from app.utils.db import get_db_connection
import json

class TarjetasRepository:
    @staticmethod
    def get_all(id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM public."Tarjeta" WHERE "idUser" = %s;', (id,))
        tarjetasData = cursor.fetchall()
        cursor.close()
        conn.close()
        tarjetas = [{'nombre': row[4], 'cantidad': row[1], 'gastosList': row[2], 'ingresosList': row[3], 'idTarjeta': row[0]} for row in tarjetasData]
        return tarjetas 

    @staticmethod
    def get_by_id(id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM public."Tarjeta" WHERE "idTarjeta" = %s;', (id,))
        tarjetas = cursor.fetchone()
        cursor.close()
        conn.close()
        tarjetas = {'name': tarjetas[4], 'amount': tarjetas[1], 'listIdGastos': tarjetas[2], 'listIdIngresos': tarjetas[3], 'idTarjeta': tarjetas[0]}
        return tarjetas

    @staticmethod
    def create(data):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                'INSERT INTO public."Tarjeta" (amount, "listIdGastos", "listIdIngresos", name, "idTipo", "idUser") VALUES (%s, %s, %s, %s, %s, %s);',
                (data['amount'], data.get('listIdGastos', []), data.get('listIdIngresos', []), data['name'], data['idTipo'], data['idUser'])
            )
            conn.commit()
            return {'message': 'Tarjeta creada correctamente'}
        except Exception as e:
            conn.rollback()
            return {'error': str(e)}
        finally:
            cursor.close()
            conn.close()


    @staticmethod
    def update(id, data):
        print(data)
        print(id)
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE public."Tarjeta" SET amount = %s, name = %s WHERE "idTarjeta" = %s;',
            (data['amount'], data['name'], id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return {'id': id, **data}

    @staticmethod
    def delete(id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM public."Tarjeta" WHERE "idTarjeta" = %s;', (id,))
        conn.commit()
        cursor.close()
        conn.close()
