from app.database import db

#paquetes viajes

class PaquetesViaje(db.Model):
    __tablename__ = 'PaquetesViaje'

    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Destino = db.Column(db.String(100))
    Descripcion = db.Column(db.Text)
    Precio = db.Column(db.Numeric(10, 2))
    Imagen = db.Column(db.String(100))

#Consultas

class Consultas(db.Model):
    __tablename__ = 'Consultas'

    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    PaqueteId = db.Column(db.Integer, db.ForeignKey('PaquetesViaje.Id'))
    Nombre = db.Column(db.String(100))
    Email = db.Column(db.String(100))
    Mensaje = db.Column(db.Text)
    Fecha = db.Column(db.DateTime, default=db.func.current_timestamp())
    Whatsapp = db.Column(db.String(50))

    paquete = db.relationship('PaquetesViaje', backref='consultas')
