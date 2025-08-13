import sqlite3
import csv
import os

db_path = "app/viajes.db"
csv_path = "app/consultas.csv"

# Asegurarse de que la carpeta exista
os.makedirs(os.path.dirname(csv_path), exist_ok=True)

# Conectar a la base
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Exportar datos de Consultas
cursor.execute("SELECT nombre, email, mensaje, fecha, whatsapp FROM Consultas ORDER BY fecha DESC")
filas = cursor.fetchall()

# Encabezados
encabezados = ["nombre", "email", "mensaje", "fecha", "whatsapp"]

# Escribir CSV
with open(csv_path, mode="w", newline="", encoding="utf-8") as archivo_csv:
    writer = csv.writer(archivo_csv)
    writer.writerow(encabezados)
    writer.writerows(filas)

conn.close()

print(f"✅ Exportación completa: {csv_path}")
