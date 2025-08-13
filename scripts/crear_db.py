from app import app
from app import conn  # si estás usando pyodbc

cursor = conn.cursor()

# Ejemplo: crear tabla paquetes
cursor.execute("""
CREATE TABLE PaquetesViaje (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Destino NVARCHAR(100),
    Descripcion NVARCHAR(MAX),
    Precio DECIMAL(10,2),
    Imagen NVARCHAR(100),
)
""")

conn.commit()
print("✅ Tabla creada con éxito")

