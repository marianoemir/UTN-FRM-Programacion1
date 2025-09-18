# PRACTICA INTEGRADORA 1 – PYTHON 

golosinas = [
    [1, "KitKat", 20], [2, "Chicles", 50], [3, "Caramelos de Menta", 50],
    [4, "Huevo Kinder", 10], [5, "Chetoos", 10], [6, "Twix", 10],
    [7, "M&M'S", 10], [8, "Papas Lays", 2], [9, "Milkybar", 10],
    [10, "Alfajor Tofi", 15], [11, "Lata Coca", 20], [12, "Chitos", 10]
]

empleados = {
    1100: "José Alonso", 1200: "Federico Pacheco",
    1300: "Nelson Pereira", 1400: "Osvaldo Tejada",
    1500: "Gastón Garcia"
}

clavesTecnico = ("admin", "CCCDDD", "2020")
golosinasPedidas = []



def pedir_golosina():
    numero_legajo = int(input("Ingrese su numero de legajo: "))
    if numero_legajo in empleados:
        while True:
            for g in golosinas:
                print(f"Código: {g[0]} | Nombre: {g[1]} | Stock: {g[2]}")
            
            eleccion_del_usuario = int(input("Introduzca el codigo de la golosina que desea: "))
            
            for g in golosinas:
                if g[0] == eleccion_del_usuario:
                    if g[2] > 0:
                        g[2] -= 1
                        golosinasPedidas.append(g[1])
                        print(f"Usted ha pedido {g[1]}")
                    else:
                        print(f"Lo sentimos la golosina {g[1]} no se encuentra disponible.")
                    break  
            
            otra = input("Desea pedir otra golosina? (s/n): ").lower()
            if otra != 's':
                break
    else:
        print("Usted no es parte de la empresa")


def mostrar_golosinas():
    print("\nGolosinas disponibles:")
    for g in golosinas:
        print(f"Código: {g[0]} | Nombre: {g[1]} | Stock: {g[2]}")
    print()


def rellenar_golosina():
    print("\nAcceso técnico requerido")
    clave1 = input("Ingrese la primera clave: ")
    clave2 = input("Ingrese la segunda clave: ")
    clave3 = input("Ingrese la tercera clave: ")

    if (clave1, clave2, clave3) == clavesTecnico:
        print("Acceso autorizado. Puede recargar golosinas.")
        codigo = int(input("Ingrese el código de la golosina a recargar: "))
        for g in golosinas:
            if g[0] == codigo:
                cantidad = int(input(f"Ingrese la cantidad a recargar para {g[1]}: "))
                if cantidad > 0:
                    g[2] += cantidad
                    print(f"Se han recargado {cantidad} unidades de {g[1]}. Stock actual: {g[2]}")
                else:
                    print("La cantidad debe ser mayor a cero.")
                break
    else:
        print("No tiene permiso para ejecutar la función de recarga.")


def apagar_maquina():
    print("\nApagando la máquina…")
    print("Golosinas pedidas durante la sesión:")
    for g in golosinasPedidas:
        print(f"- {g}")
    print(f"Total de golosinas pedidas: {len(golosinasPedidas)}")


bucle_principal = True
while bucle_principal:
    eleccion = int(input("1.Pedir Golosina.\n"
                        "2.Mostrar Golosina.\n"
                        "3.Rellenar Golosina.\n"
                        "4.Apagar Maquina.\n"
                        "Seleccione una opción: "))

    if eleccion == 1:
        pedir_golosina()
    elif eleccion == 2:
        mostrar_golosinas()
    elif eleccion == 3:
        rellenar_golosina()
    elif eleccion == 4:
        apagar_maquina()
        bucle_principal = False
