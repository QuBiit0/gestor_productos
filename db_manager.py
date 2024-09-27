import sqlite3
from productos import Producto

class DBManager:
    def __init__(self, db_name='productos.db'):
        """Inicializa la conexión a la base de datos SQLite."""
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.create_table()

    def create_table(self):
        """Crea la tabla de productos si no existe."""
        try:
            with self.conn:
                self.conn.execute('''
                    CREATE TABLE IF NOT EXISTS productos (
                        id_producto INTEGER PRIMARY KEY,
                        nombre TEXT NOT NULL,
                        tipo TEXT NOT NULL,
                        precio REAL NOT NULL
                    );
                ''')
        except sqlite3.Error as e:
            print(f"Error creando la tabla: {e}")

    def agregar_producto(self, producto):
        """Inserta un producto en la base de datos."""
        try:
            with self.conn:
                self.conn.execute('''
                    INSERT INTO productos (id_producto, nombre, tipo, precio)
                    VALUES (?, ?, ?, ?)
                ''', (producto.id_producto, producto.nombre, producto.tipo, producto.precio))
        except sqlite3.IntegrityError:
            print(f"Error: el ID {producto.id_producto} ya existe.")
        except sqlite3.Error as e:
            print(f"Error al insertar producto: {e}")

    def obtener_producto(self, id_producto):
        """Devuelve un producto a partir de su ID."""
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM productos WHERE id_producto = ?", (id_producto,))
            row = cur.fetchone()
            if row:
                return Producto(*row)
            else:
                print(f"Producto con ID {id_producto} no encontrado.")
                return None
        except sqlite3.Error as e:
            print(f"Error al obtener producto: {e}")

    def actualizar_precio_producto(self, id_producto, nuevo_precio):
        """Actualiza el precio de un producto en la base de datos."""
        try:
            with self.conn:
                self.conn.execute('''
                    UPDATE productos
                    SET precio = ?
                    WHERE id_producto = ?
                ''', (nuevo_precio, id_producto))
        except sqlite3.Error as e:
            print(f"Error al actualizar el precio: {e}")

    def eliminar_producto(self, id_producto):
        """Elimina un producto de la base de datos."""
        try:
            with self.conn:
                self.conn.execute('''
                    DELETE FROM productos
                    WHERE id_producto = ?
                ''', (id_producto,))
        except sqlite3.Error as e:
            print(f"Error al eliminar el producto: {e}")

    def listar_productos(self):
        """Lista todos los productos almacenados en la base de datos."""
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM productos")
            productos = cur.fetchall()
            return [Producto(*row) for row in productos]
        except sqlite3.Error as e:
            print(f"Error al listar productos: {e}")
            return []
