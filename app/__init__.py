from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()

from .modelos import Usuario  # Importa el modelo de Usuario

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'tu_clave_secreta'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tienda.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Configuración de Flask-Mail
    app.config['MAIL_SERVER'] = 'smtp.example.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'tu_email@example.com'
    app.config['MAIL_PASSWORD'] = 'tu_contraseña'

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'rutas.iniciar'
    mail.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.get(user_id)

    with app.app_context():
        from . import modelos
        db.create_all()

    # Registrar Blueprints
    from .rutas import bp as rutas_blueprint
    app.register_blueprint(rutas_blueprint)
    
    return app
