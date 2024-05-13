from app import create_app
# Importa la función create_app desde el módulo app.


# Crea una instancia de la aplicación Flask.
app = create_app()

# Si este archivo se ejecuta directamente...
if __name__ == '__main__':
    # ...inicia el servidor de desarrollo de Flask.
    app.run(debug=True)
