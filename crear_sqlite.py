import sqlite3
import csv
import os

if os.path.exists("app/viajes.db"):
    os.remove("app/viajes.db")

os.makedirs("app", exist_ok=True)
conn = sqlite3.connect("app/viajes.db")
cursor = conn.cursor()

# Crear tabla Consultas
cursor.execute("""
CREATE TABLE IF NOT EXISTS Consultas (
    Id INTEGER PRIMARY KEY,
    paqueteId INTEGER,
    nombre TEXT,
    email TEXT,
    mensaje TEXT,
    fecha TEXT,
    whatsapp TEXT
)
""")

# Crear tabla PaquetesViaje
cursor.execute("""
CREATE TABLE IF NOT EXISTS PaquetesViaje (
    Id INTEGER PRIMARY KEY,
    destino TEXT,
    descripcion TEXT,
    precio REAL,
    imagen TEXT
)
""")

# Cargar Consultas
with open("Consultas.csv", newline='', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=';')
    reader.fieldnames = [key.strip() for key in reader.fieldnames]
    for row in reader:
        row = {k.strip(): v.strip() for k, v in row.items()}
        try:
            cursor.execute("""
                INSERT INTO Consultas (Id, paqueteId, nombre, email, mensaje, fecha, whatsapp)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                int(row['Id']),
                row['paqueteId'],
                row['nombre'],
                row['email'],
                row['mensaje'],
                row['fecha'],
                row['whatsapp']
            ))
        except Exception as e:
            print(f"❌ Fila inválida: {row} → {e}")

# Cargar Paquetes
with open("PaqueteViajes.csv", newline='', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, delimiter=';')
    reader.fieldnames = [key.strip() for key in reader.fieldnames]
    for row in reader:
        row = {k.strip(): v.strip() for k, v in row.items()}
        try:
            cursor.execute("""
                INSERT INTO PaquetesViaje (Id, destino, descripcion, precio, imagen)
                VALUES (?, ?, ?, ?, ?)
            """, (
                int(row['Id']),
                row['destino'],
                row['descripcion'],
                float(row['precio']),
                row['imagen']
            ))
        except Exception as e:
            print(f"❌ Fila inválida: {row} → {e}")

conn.commit()
conn.close()
print("✅ Base SQLite creada con datos")
