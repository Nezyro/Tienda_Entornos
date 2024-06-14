from . import db
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(150), unique=True, nullable=False)
    nombre = db.Column(db.String(150), nullable=False)
    contraseña = db.Column(db.String(150), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Usuario {self.nombre}>"

class Categoria(db.Model):
    __tablename__ = 'categorias'
    id_categoria = db.Column(db.Integer, primary_key=True)
    nombre_categoria = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Categoria {self.nombre_categoria}>"

class Producto(db.Model):
    __tablename__ = 'productos'
    id_producto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    imagen = db.Column(db.String(255))
    descripcion = db.Column(db.String(255))
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id_categoria'), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Float, nullable=False)
    
    categoria = db.relationship('Categoria', backref=db.backref('productos', lazy=True))

    def __repr__(self):
        return f"<Producto {self.nombre}>"

class Carrito(db.Model):
    __tablename__ = 'carritos'
    id = db.Column(db.Integer, primary_key=True)
    usuario_correo = db.Column(db.String(120), db.ForeignKey('usuarios.correo'), nullable=False)
    
    usuario = db.relationship('Usuario', backref=db.backref('carritos', lazy=True))

    def __repr__(self):
        return f"<Carrito {self.id}>"

class ItemCarrito(db.Model):
    __tablename__ = 'items_carrito'
    id_item_carrito = db.Column(db.Integer, primary_key=True)
    carrito_id = db.Column(db.Integer, db.ForeignKey('carritos.id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id_producto'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False, default=1)  # Nuevo atributo cantidad

    carrito = db.relationship('Carrito', backref=db.backref('items_carrito', lazy=True))
    producto = db.relationship('Producto', backref=db.backref('items_carrito', lazy=True))

    def __repr__(self):
        return f"<ItemCarrito {self.id_item_carrito}>"

