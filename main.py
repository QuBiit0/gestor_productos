from db_manager import DBManager
from productos import Producto

def main():
    db = DBManager()

    # Menú simple para interactuar con el sistema
    while True:
        print("\n1. Agregar producto")
        print("2. Listar productos")
        print("3. Actualizar precio")
        print("4. Eliminar producto")
        print("5. Salir")
        
        opcion = input("\nSelecciona una opción: ")

        if opcion == '1':
            id_producto = int(input("ID del producto: "))
            nombre = input("Nombre del producto: ")
            tipo = input("Tipo de producto: ")
            precio = float(input("Precio del producto: "))
            nuevo_producto = Producto(id_producto, nombre, tipo, precio)
            db.agregar_producto(nuevo_producto)

        elif opcion == '2':
            productos = db.listar_productos()
            for producto in productos:
                print(producto)

        elif opcion == '3':
            id_producto = int(input("ID del producto a actualizar: "))
            nuevo_precio = float(input("Nuevo precio: "))
            db.actualizar_precio_producto(id_producto, nuevo_precio)

        elif opcion == '4':
            id_producto = int(input("ID del producto a eliminar: "))
            db.eliminar_producto(id_producto)

        elif opcion == '5':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
