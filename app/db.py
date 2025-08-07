import os

db_engine = os.getenv("DB_ENGINE", "sqlserver")

if db_engine == "sqlite":
    import sqlite3
    db_path = os.path.join(os.path.dirname(__file__), '..', 'database', 'mydb.db')
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path, check_same_thread=False)

    def init_db():
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS PaquetesViaje (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                destino TEXT,
                descripcion TEXT,
                precio REAL,
                imagen TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Consultas (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                PaqueteId INTEGER,
                Nombre TEXT,
                Email TEXT,
                Whatsapp TEXT,
                Mensaje TEXT
            )
        """)
        conn.commit()
else:
    import pyodbc
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=MSI\\SQLEXPRESS;'
        'DATABASE=AgenciaViajes;'
        'Trusted_Connection=yes;'
    )

    def init_db():
        pass  # No hace falta inicializar tablas en SQL Server desde Flask

