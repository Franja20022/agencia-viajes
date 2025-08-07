from flask import Flask
from database import init_app, db
from models_for_render import PaquetesViaje, Consultas   # Importá todos tus modelos

app = Flask(__name__)
init_app(app)

with app.app_context():
    db.create_all()  # Crea las tablas en SQLite si no existen
