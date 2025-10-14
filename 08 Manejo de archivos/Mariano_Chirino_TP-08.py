def leer_productos(nombre_archivo):
    productos = []


    archivo = open(nombre_archivo, "a")  
    archivo.close()                   

    archivo = open(nombre_archivo, "r")  
    for linea in archivo:
        if linea.strip() != "":
            nombre, precio, cantidad = linea.strip().split(",")
            productos.append({
                "nombre": nombre,
                "precio": float(precio),
                "cantidad": int(cantidad)
            })
    archivo.close()
    return productos


def mostrar_productos(productos):
    if len(productos) == 0:
        print("\nNo hay productos cargados.\n")
    else:
        print("\n--- Lista de productos ---")
        for p in productos:
            print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
        print("---------------------------\n")


def agregar_producto(productos):
    print("\n--- Agregar producto ---")
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio: "))
    cantidad = int(input("Ingrese la cantidad: "))
    productos.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })
    print(f"Producto '{nombre}' agregado correctamente.\n")


def buscar_producto(productos):
    nombre_buscar = input("\nIngrese el nombre del producto a buscar: ")
    encontrado = False
    for p in productos:
        if p["nombre"].lower() == nombre_buscar.lower():
            print("\nProducto encontrado:")
            print(f"Nombre: {p['nombre']}")
            print(f"Precio: ${p['precio']}")
            print(f"Cantidad: {p['cantidad']}\n")
            encontrado = True
    if not encontrado:
        print("Producto no encontrado.\n")


def guardar_productos(nombre_archivo, productos):
    archivo = open(nombre_archivo, "w")
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
    archivo.close()
    print("Productos guardados correctamente.\n")


def main():
    ARCHIVO = "productos.txt"
    productos = leer_productos(ARCHIVO)

    while True:
        print("===== MENÚ =====")
        print("1. Mostrar productos")
        print("2. Agregar producto")
        print("3. Buscar producto")
        print("4. Guardar y salir")
        print("================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_productos(productos)
        elif opcion == "2":
            agregar_producto(productos)
        elif opcion == "3":
            buscar_producto(productos)
        elif opcion == "4":
            guardar_productos(ARCHIVO, productos)
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida, intente nuevamente.\n")


main()
