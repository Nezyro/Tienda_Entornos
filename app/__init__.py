from flask import Flask
from . import rutas

def create_app():
    # Crea una instancia de la aplicación Flask
    app = Flask(__name__)

    # Configuraciones, extensiones, rutas, etc.
    app.register_blueprint(rutas.bp)
    
    return app
