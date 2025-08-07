import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()  # Carga las variables del archivo .env si estás en local

db = SQLAlchemy()

def init_app(app):
    engine = os.getenv('DB_ENGINE', 'sqlite')  # Por defecto usa SQLite

    if engine == 'sqlserver':
        # Conexión local a SQL Server
        app.config['SQLALCHEMY_DATABASE_URI'] = (
            'mssql+pyodbc://@MSI\\SQLEXPRESS/AgenciaViajes?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes'
        )
    else:
        # Conexión en Render con SQLite
        db_path = os.path.join(os.path.dirname(__file__), 'database', 'agencia.db')
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

