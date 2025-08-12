from flask import Flask, render_template, request, redirect, url_for
from .db import conn, init_db
import sqlite3

app = Flask(__name__)
init_db()  # Crea tablas si usás SQLite

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/agencia')
def agencia():
    cursor = conn.cursor()
    cursor.execute("SELECT Id, destino, descripcion, precio, imagen FROM PaquetesViaje")
    columns = [column[0] for column in cursor.description]
    PaquetesViaje = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return render_template('agencia.html', PaquetesViaje=PaquetesViaje)

@app.route('/mirador360')
def negocio_mirador360():
    return render_template('mirador360.html')

@app.route('/experiencias')
def negocio_experiencias():
    return render_template('experiencias.html')

@app.route('/consulta', methods=['POST'])
def enviar_consulta():
    paquete_id = request.form.get('paquete_id')
    destino = request.form.get('destino')
    descripcion = request.form.get('descripcion')
    precio = request.form.get('precio')
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    whatsapp = request.form.get('whatsapp')
    mensaje = request.form.get('mensaje')

    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Consultas (PaqueteId, Nombre, Email, Whatsapp, Mensaje)
        VALUES (?, ?, ?, ?, ?)
    """, (paquete_id, nombre, email, whatsapp, mensaje))
    conn.commit()

    return redirect(url_for('consulta_enviada', destino=destino))

@app.route('/consulta-enviada')
def consulta_enviada():
    destino = request.args.get('destino')
    return render_template('consulta_enviada.html', destino=destino)

@app.route('/consulta/<int:paquete_id>', methods=['GET'])
def consulta(paquete_id):
    cursor = conn.cursor()
    cursor.execute("SELECT Id, destino, descripcion, precio FROM PaquetesViaje WHERE Id = ?", paquete_id)
    paquete = cursor.fetchone()

    if paquete:
        return render_template('consulta.html', paquete=paquete)
    else:
        return "Paquete no encontrado", 404
