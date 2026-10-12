
import mysql.connector


def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="fastapi_pdbc",
        password="fastapi_pdbc@123",
        database="fastapipdbc"
    )

    return connection
