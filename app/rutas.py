from flask import Blueprint, render_template, flash, redirect, url_for, request, abort
from flask_login import login_user, current_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from .formularios import RegistroForm, LoginForm
from .modelos import Usuario, Producto, ItemCarrito, Categoria, Carrito, db
import os
from flask_mail import Message
from . import mail
from functools import wraps

bp = Blueprint('rutas', __name__)

# Definir el manejador de errores 404
@bp.app_errorhandler(404)
def page_not_found(error):
    return redirect(url_for('rutas.iniciar'))

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            abort(403)  # Forbidden
        return f(*args, **kwargs)
    return decorated_function

@bp.route('/')
def index():
    productos = Producto.query.all()
    return render_template('index.html', productos=productos, current_user=current_user)

@bp.route('/iniciar', methods=["GET", "POST"])
def iniciar():
    if current_user.is_authenticated:
        return redirect(url_for('rutas.index'))
    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(correo=form.email.data).first()
        if usuario and check_password_hash(usuario.contraseña, form.password.data):
            login_user(usuario)
            flash('Inicio de sesión exitoso!', 'success')
            return redirect(url_for('rutas.index'))
        else:
            flash('Correo o contraseña incorrectos.', 'danger')
    return render_template('iniciar.html', form=form, current_user=current_user)

@bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if current_user.is_authenticated:
        return redirect(url_for('rutas.index'))
    form = RegistroForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
        nuevo_usuario = Usuario(correo=form.email.data, nombre=form.usuario.data, contraseña=hashed_password)
        db.session.add(nuevo_usuario)
        db.session.commit()
        flash('Registro exitoso! Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('rutas.iniciar'))
    return render_template('registro.html', form=form, current_user=current_user)


@bp.route('/cerrar_sesion')
@login_required
def cerrar_sesion():
    logout_user()
    flash('Has cerrado sesión correctamente', 'success')
    return redirect(url_for('rutas.index'))

@bp.route('/carrito', methods=['GET', 'POST'])
@login_required
def carrito():
    carrito = Carrito.query.filter_by(usuario_correo=current_user.correo).first()
    return render_template('carrito.html', carrito=carrito, current_user=current_user)

@bp.route('/producto/<int:producto_id>')
def producto(producto_id):
    producto = Producto.query.get_or_404(producto_id)
    return render_template('producto.html', producto=producto, current_user=current_user)

@bp.route('/agregar_al_carrito/<int:producto_id>', methods=["GET", "POST"])
@login_required
def agregar_al_carrito(producto_id):
    producto = Producto.query.get_or_404(producto_id)
    carrito = current_user.carritos[0] if current_user.carritos else Carrito(usuario=current_user)
    nuevo_item_carrito = ItemCarrito(carrito=carrito, producto=producto)
    db.session.add(nuevo_item_carrito)
    db.session.commit()
    flash(f'{producto.nombre} ha sido agregado al carrito', 'success')
    return redirect(url_for('rutas.carrito'))

@bp.route('/eliminar_item_carrito/<int:item_id>', methods=['POST'])
@login_required
def eliminar_item_carrito(item_id):
    item = ItemCarrito.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    flash('El item ha sido eliminado del carrito', 'success')
    return redirect(url_for('rutas.carrito'))

@bp.route('/registro_categoria', methods=['GET', 'POST'])
@admin_required
def registro_categoria():
    if request.method == 'POST':
        nombre_categoria = request.form['nombre_categoria']
        nueva_categoria = Categoria(nombre_categoria=nombre_categoria)
        db.session.add(nueva_categoria)
        db.session.commit()
        flash('Categoría registrada exitosamente!', 'success')
        return redirect(url_for('rutas.registro_categoria'))
    return render_template('registro_categoria.html', current_user=current_user)

@bp.route('/registro_producto', methods=['GET', 'POST'])
@admin_required
def registro_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        categoria_id = request.form['categoria']
        stock = int(request.form['stock'])
        precio = float(request.form['precio'])
        imagen = request.files['imagen']

        # Crear el nuevo producto sin establecer la imagen todavía
        nuevo_producto = Producto(nombre=nombre, descripcion=descripcion, categoria_id=categoria_id, stock=stock, precio=precio)

        # Agregar y confirmar el nuevo producto para obtener su ID
        db.session.add(nuevo_producto)
        db.session.commit()
        id_producto = nuevo_producto.id_producto  # Obtener el ID después de confirmar

        # Verificar si se proporcionó una imagen, si no, usar la imagen predeterminada
        if not imagen or imagen.filename == '':
            # Establecer la ruta predeterminada para la imagen del producto
            imagen_path = 'imgs/productos/default_producto.png'  # Cambia esto con la ruta real de tu imagen predeterminada
        else:
            # Guardar la imagen con el nombre del ID del producto
            imagen_extension = os.path.splitext(imagen.filename)[1]  # Obtener la extensión de la imagen
            imagen_filename = f"{id_producto}{imagen_extension}"  # Nombre de la imagen con el ID del producto y su extensión
            imagen_path = f'imgs/productos/{imagen_filename}'
            imagen.save(os.path.join(bp.root_path, 'static', imagen_path))

        # Actualizar el producto con la ruta de la imagen y guardar los cambios
        nuevo_producto.imagen = imagen_path
        db.session.commit()

        flash('Producto registrado exitosamente!', 'success')
        return redirect(url_for('rutas.producto', producto_id=nuevo_producto.id_producto))
    
    categorias = Categoria.query.all()
    return render_template('registro_producto.html', categorias=categorias, current_user=current_user)

@bp.route('/comprobar_pago', methods=['GET', 'POST'])
@login_required
def comprobar_pago():
    carrito = current_user.carritos[0] if current_user.carritos else None
    if carrito:
        for item in carrito.items_carrito:
            db.session.delete(item)
        db.session.commit()
        flash('Pago realizado con éxito y carrito vaciado', 'success')
    return render_template('pago.html', current_user=current_user)

def enviar_correo_confirmacion(usuario, carrito):
    msg = Message('Confirmación de Compra', sender='tu_email@example.com', recipients=[usuario.correo])
    msg.body = f"Hola {usuario.nombre},\n\nTu compra ha sido confirmada. Aquí tienes los detalles de tu compra:\n\n"
    for item in carrito.items:
        msg.body += f"- {item.producto.nombre}: {item.producto.precio} €\n"
    msg.body += "\nGracias por tu compra.\n\nSaludos,\nEquipo de Sant Josep Obrer"

    mail.send(msg)

@bp.route('/eliminar_producto/<int:producto_id>', methods=['POST'])
@admin_required
def eliminar_producto(producto_id):
    producto = Producto.query.get_or_404(producto_id)
    db.session.delete(producto)
    db.session.commit()
    flash('Producto eliminado correctamente', 'success')
    return redirect(url_for('rutas.index'))