import mysql.connector
from mysql.connector import Error
def create_database():
    try:
        connection = mysql.connector.connect(
            host = '127.0.0.1'
            user = 'root'
            password = 'Cadeau@0707'
        )
        if connection.is_connected():
            cursor = connection.cursor()
            create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
            cursor.execute(create_db_query)
            print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
create_database()  #calling the function
