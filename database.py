import pyodbc
from config import DB_CONFIG

def get_connection():
    conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=MSI\SQLEXPRESS;'
    'DATABASE=AgenciaViajes;'
    'Trusted_Connection=yes;'
    )
    return conn
