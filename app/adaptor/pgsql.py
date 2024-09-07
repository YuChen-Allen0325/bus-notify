import logging.config

import psycopg2.extras
import psycopg2

from app.config import PostgresConfig

log = logging.getLogger(__name__)

_connection = None
_cursor = None


def init():
    global _connection
    global _cursor

    try:
        _connection = psycopg2.connect(
            host=PostgresConfig.URL,
            dbname=PostgresConfig.DB_NAME,
            user=PostgresConfig.USERNAME,
            password=PostgresConfig.PASSWORD,
            port=PostgresConfig.PORT,
            keepalives=1,
            keepalives_idle=60,
            keepalives_interval=10,
            keepalives_count=15
        )
        _cursor = _connection.cursor(
            cursor_factory=psycopg2.extras.RealDictCursor)

    except Exception as e:
        log.critical(e, exc_info=True)
        _connection.close()
    log.info("pgsql init")
    return True


def query(sql_string, sql_args={}):
    try:
        rows = {}

        _cursor.execute(sql_string, sql_args)
        rows = _cursor.fetchall()
        _connection.commit()

        return rows
    except Exception as e:
        _connection.rollback()


def commit(sql_string, sql_args):
    try:
        _cursor.execute(sql_string, sql_args)
        _connection.commit()
        return _cursor.lastrowid
    except Exception as e:
        _connection.rollback()

def get_user_reservation_information():   ## notify_flag = 0 代表還未通知過
    try: 
        sql_stmt = """
            SELECT * 
            FROM bus_notify_information
            WHERE notify_flag = 0
            """
        data = {
        }

        return query(sql_stmt, data)
    except (psycopg2.InterfaceError, psycopg2.OperationalError)as e:
        init()
        return query(sql_stmt, data)
    except Exception as e:
        log.error(f"get_user_reservation_information error: {e}")


def update_notify_flag(id):
    try:
        sql_stmt = """
            UPDATE bus_notify_information
            SET notify_flag = 1
            WHERE id = %(id)s
        """

        data = {
            'id': id
        }

        commit(sql_stmt, data)
    except (psycopg2.InterfaceError, psycopg2.OperationalError)as e:
        init()
        commit(sql_stmt, data)
    except Exception as e:
        log.error(f'update_notify_flag error: {e}')