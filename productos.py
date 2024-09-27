class Producto:
    def __init__(self, id_producto, nombre, tipo, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Tipo: {self.tipo}, Precio: {self.precio}"

    def actualizar_precio(self, nuevo_precio):
        """Actualiza el precio del producto."""
        self.precio = nuevo_precio
