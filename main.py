from app import app
import os

if __name__ == '__main__':
    app.run(debug=True)

if os.getenv("DB_ENGINE") == "sqlite":
    import crear_db_render  # Esto ejecuta el script al iniciar