from flask import Blueprint, render_template

# Crea un Blueprint para las rutas
bp = Blueprint('routes', __name__)

# Ruta para la página de inicio
@bp.route('/')
def index():
    return render_template('index.html')

# Ruta para la página de categorías
@bp.route('/categorias')
def categorias():
    # Aquí podrías obtener la lista de categorías desde tu base de datos
    categorias = ['Electrónica', 'Ropa', 'Hogar']
    return render_template('categorias.html', categorias=categorias)

# Ruta para la página de inicio de sesión
@bp.route('/iniciar_sesion')
def iniciar_sesion():
    return render_template('iniciar_sesion.html')

# Ruta para la página de registro
@bp.route('/registro')
def registro():
    return render_template('registro.html')

# Ruta para la página del carrito de compras
@bp.route('/carrito')
def carrito():
    return render_template('carrito.html')

# Ruta para la página de un producto específico
@bp.route('/producto/<int:producto_id>')
def producto(producto_id):
    # Aquí podrías obtener información sobre el producto con el ID dado desde tu base de datos
    # Luego, renderiza una plantilla que muestre la información del producto
    return render_template('producto.html', producto_id=producto_id)
