# Proyecto: Tienda en línea con Flask

## Descripción del proyecto:

El objetivo de este proyecto es desarrollar una aplicación web para una tienda en línea utilizando el framework Flask de Python. La tienda permitirá a los usuarios navegar por diferentes categorías de productos, agregar productos a su carrito de compra y realizar pedidos.

## Funcionalidades principales:

1. **Sección 1. Registro y autenticación de usuarios:**
   - Los usuarios podrán registrarse en la tienda proporcionando un nombre de correo electrónico y contraseña.
   - Los usuarios podrán iniciar sesión en la tienda utilizando su correo electrónico y contraseña.

2. **Sección 2. Dar de alta productos y categorías:**
   - Habrá una sección para dar de alta los productos. Los campos serán "nombre", "descripción", "categoría" e "imagen".

      Nota: En la bbdd lo que guardaremos es la ruta donde se guarda nuestra imagen. Concretamente estas estarán dentro de `static/imgs/`.

   - Habrá una sección para dar de alta las categorías de los productos. El campo será "nombre". 

3. **Sección 3. Visualización de productos:**
   - Los usuarios podrán navegar por las diferentes categorías de productos disponibles en la tienda.
   - Se mostrará una lista de productos en cada categoría, con información detallada como nombre, descripción, precio y disponibilidad.

4. **Sección 4. Carrito de compra:**
   - Los usuarios podrán agregar productos al carrito de compra desde la página de detalles del producto.
   - Los usuarios podrán ver los productos en su carrito de compra, el precio total, así como modificar la cantidad o eliminar productos.
      - Cómo no hemos practicado `JS`, eliminar el producto se podrá hacer teniendo un 0 en el valor de la cantidad.

5. **Sección 5. Proceso de compra:**
   - Los usuarios podrán validar el carrito y "comprar" esos productos. Saldrá un mensaje para confirmar que efectivamente quieren realizar la compra, así cómo el importe total.

## Consideraciones adicionales:

- El proyecto se entregará como un repositorio de Git que contenga todo el código fuente, así como cualquier archivo de configuración o dependencia necesaria.
- Se debe proporcionar un archivo README.md que describa brevemente el proyecto, cómo instalar y ejecutar la aplicación, y cualquier otra información relevante para los usuarios y desarrolladores.
- Se deberá proporcionar también un archivo con el esquema de las tablas y las relaciones de la base de datos necesarias para montar el servidor y que así los compañeros de ASIX puedan configurar el servidor de BBDD.

## Grupos de trabajo:

- Grupo 1: A. Arjona, F. Gómez, M. Soliz.
- Grupo 2: J. Cifre, N. Gómez, F. Planas.
- Grupo 3: M. Colom, J. González.
- Grupo 4: A. Foguet, J. Pericás, M. Molines.
- Grupo 5: O. Girao, R. Martín, F. Pérez.

## Entrega del proyecto:

- El proyecto se entregará como un repositorio de Git que contenga todo el código fuente, así como cualquier archivo de configuración o dependencia necesaria.
- Se debe proporcionar un archivo README.md que describa brevemente el proyecto, cómo instalar y ejecutar la aplicación, y cualquier otra información relevante para los usuarios y desarrolladores.
