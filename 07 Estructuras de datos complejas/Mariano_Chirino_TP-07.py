#Ejercicio 1

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

for clave, valor in precios_frutas.items():
    print(f"Clave: {clave}, Valor: {valor}")

#Ejercicio 2

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print("")
for clave, valor in precios_frutas.items():
    print(f"Clave: {clave}, Valor: {valor}")

#Ejercicio 3

frutas_sin_precios = (list(precios_frutas))

print("")

for r in frutas_sin_precios:
    print(f"Fruta: {r}")

#Ejercicio 4

contactos = {}

print("")

for i in range(5):
    print(f"Ingrese el numero de contacto {i + 1} de 5")

    while True:
        nombre = input(" Nombre: ")
        if nombre:
            break  
        print(" El nombre no puede estar vacio intentelo de nuevo.")

    while True:
        numero = input(" Numero de telefono (solo digitos): ")
        
        if numero:
            break
        print(" El numero de telefono no puede estar vacio")

    contactos[nombre] = numero
    print(f"  {nombre} agregado.")

print("\n--- CARGA FINALIZADA ---")
print(contactos)

print("\n--- CONSULTA DE NÚMEROS ---")

while True:
    nombre_consulta = input(
        "\nIngrese el nombre del contacto a buscar (o '0' para terminar): "
    )

    if nombre_consulta == "0":
        print("Programa terminado.")
        break

    numero_asociado = contactos.get(nombre_consulta)

    if numero_asociado:
        print(f" El número de {nombre_consulta} es: {numero_asociado}")
    else:
        print(f" El contacto '{nombre_consulta}' no se encuentra en la agenda.")

# Ejercicio 5
print("")
frase = input("Ingrese una frase: ").lower().split()

palabras_unicas = set(frase)
frecuencias = {}

for palabra in frase:
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

print("\nPalabras únicas:", palabras_unicas)
print("Frecuencia de cada palabra:", frecuencias)

#Ejercicio 6
print("")

alumnos = {}

for i in range(3):
    nombre = input(f"\nIngrese el nombre del alumno {i+1}: ")
    notas = []
    for j in range(3):
        nota = float(input(f" Ingrese la nota {j+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

print("\n--- Promedios ---")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

# Ejercicio 7

print("")
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7}

print("\nAprobaron ambos parciales:", parcial1 & parcial2)
print("Aprobaron solo uno:", parcial1 ^ parcial2)
print("Aprobaron al menos uno:", parcial1 | parcial2)

# Ejercicio 8

print("")
stock = {"Arroz": 10, "Leche": 5, "Pan": 20}

while True:
    producto = input("\nIngrese producto a consultar (o '0' para salir): ")
    if producto == "0":
        break

    if producto in stock:
        print(f"Stock actual de {producto}: {stock[producto]}")
        opcion = input("¿Desea agregar unidades? (s/n): ")
        if opcion.lower() == "s":
            cantidad = int(input(" Ingrese cantidad a agregar: "))
            stock[producto] += cantidad
            print(" Stock actualizado:", stock[producto])
    else:
        print("El producto no existe.")
        opcion = input("¿Desea agregarlo? (s/n): ")
        if opcion.lower() == "s":
            cantidad = int(input(" Ingrese stock inicial: "))
            stock[producto] = cantidad
            print(" Producto agregado.")

# Ejercicio 9
print("")
agenda = {("Lunes", "10:00"): "Reunión",
        ("Martes", "14:00"): "Clases",
        ("Viernes", "18:00"): "Cena"}

dia = input("\nIngrese un día: ")
hora = input("Ingrese una hora (HH:MM): ")

evento = agenda.get((dia, hora))
if evento:
    print(f"Actividad: {evento}")
else:
    print("No hay actividad registrada en ese día y hora.")

# Ejercicio 10
print("")
paises = {"Argentina": "Buenos Aires",
        "Chile": "Santiago",
        "Paraguay": "Asunción",
        "Brasil": "Brasilia"}

capitales = {capital: pais for pais, capital in paises.items()}

print("\nDiccionario invertido:")
print(capitales)



