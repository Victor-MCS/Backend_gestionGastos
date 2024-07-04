from flask import Blueprint, jsonify
import psycopg2

bp = Blueprint('expenses', __name__, url_prefix='/expenses')

@bp.route('/all', methods=['GET'])
def get_tables():
    try:
        conn = psycopg2.connect(
            dbname="db_controlGastos",
            user="admin",
            password="controlGasto123*",
            host="216.225.200.71",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
            AND table_type = 'BASE TABLE';
        """)
        tables = cur.fetchall()
        cur.close()
        conn.close()

        return jsonify(tables)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
