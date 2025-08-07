from flask import Flask
from app.database import init_app, db
from app.models_for_render import PaquetesViaje, Consultas   # Importá todos tus modelos

app = Flask(__name__)
init_app(app)

with app.app_context():
    db.create_all()  # Crea las tablas en SQLite si no existen

    if not PaquetesViaje.query.first():
        demo = PaquetesViaje(
            destino="Bariloche",
            descripcion="Paquete de 5 días con excursiones",
            precio=120000.00,
            imagen="bariloche.jpg"
        )
        db.session.add(demo)
        db.session.commit()
        print("✔️ Paquete demo creado correctamente.")
    else:
        print("ℹ️ La base ya contiene al menos un paquete.")
