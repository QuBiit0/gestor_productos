# Gestión de Productos con SQLite

Este proyecto permite gestionar productos utilizando programación orientada a objetos y una base de datos SQLite para la persistencia de los datos.

## Requisitos

- Python 3.x
- SQLite3 (viene preinstalado con Python)
  
## Instalación

1. Clona este repositorio: git clone https://github.com/QuBiit0/gestor_productos.git
2. Navega al directorio del proyecto: cd gestor_productos
3. Ejecuta el archivo principal: python main.py


## Funcionalidades

- **Agregar producto**: Permite agregar un nuevo producto con su ID, nombre, tipo y precio.
- **Listar productos**: Muestra todos los productos almacenados en la base de datos.
- **Actualizar precio**: Actualiza el precio de un producto existente.
- **Eliminar producto**: Elimina un producto de la base de datos.

## Notas

- Los productos se almacenan en un archivo `productos.db` generado por SQLite.
- Se ha implementado manejo de excepciones para evitar errores comunes en las operaciones con la base de datos.




