from flask import Flask, render_template
from flask import request, redirect, url_for
import pyodbc

app = Flask(__name__)

# Conexión directa con SQL Server
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=MSI\\SQLEXPRESS;'
    'DATABASE=AgenciaViajes;'
    'Trusted_Connection=yes;'
)

@app.route('/')
def index():
    cursor = conn.cursor()
    cursor.execute("SELECT Id, destino, descripcion, precio, imagen FROM PaquetesViaje")

    # Obtener nombres de columnas
    columns = [column[0] for column in cursor.description]

    # Convertir cada fila en un diccionario
    PaquetesViaje = [dict(zip(columns, row)) for row in cursor.fetchall()]

    return render_template('index.html', PaquetesViaje=PaquetesViaje)

# Rutas para envio de formulario de consulta
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