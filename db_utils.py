import pymysql
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def get_db_connection():
    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    return connection

def execute_query(query, args=()):
    connection = None
    cursor = None
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        print(f"Executing query: {query} with args: {args}")
        cursor.execute(query, args)
        connection.commit()
        print(f"Query executed successfully: {cursor.rowcount} rows affected")
        return cursor
    except pymysql.MySQLError as e:
        print(f"Error executing query: {query} with args: {args} - Error: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
