import random
from statistics import mean, median, mode

#1) Ejercicio 1

edad_del_usuario = int(input("Ingrese su edad porfavor: "))

if edad_del_usuario > 18:
    print("Es mayor de edad")

print("")

#2) Ejercio 2

nota_del_usuario = int(input("Introduzca su calificacion: "))

if nota_del_usuario >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

print("")

#3) Ejercicio 3

num_usuario = int(input("Ingrese un numero porfavor: "))

if num_usuario % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

print("")

#4) Ejercicio 4

edad_usuario_ejercicio4 = int(input("Ingrese su edad: "))

if edad_usuario_ejercicio4 < 12:
    print("Niño/a")
elif edad_usuario_ejercicio4 >= 12 and edad_usuario_ejercicio4 < 18:
    print("Adolescente")
elif edad_usuario_ejercicio4 >= 18 and edad_usuario_ejercicio4 < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

print("")

#5) Ejercicio 5

contraseña_del_usuario = input("Introduzca su contraseña: ")

if len(contraseña_del_usuario) >=8 and len(contraseña_del_usuario) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

print("")

#6) Ejercicio 6

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print("Números:", numeros_aleatorios)
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

if media > mediana > moda:
    print("Sesgo positivo (hacia la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (hacia la izquierda)")
else:
    print("Sin sesgo")

print("")

#7) Ejercicio 7

frase_palabra = input("Ingrese una palabra o frase:").lower()

ultima_letra = frase_palabra[-1]

if ultima_letra == 'a' or ultima_letra == 'e' or ultima_letra == 'i' or ultima_letra == 'o'or ultima_letra == 'u':
    print(frase_palabra +"!")
else:
    print(frase_palabra)

#8) Ejercicio 8

nombre_usuario_ejercicio8 = input("Ingrese su nombre:")
opcion = int(input("Ahora ingrese acción que desea realizar:\n"
"1. Si quiere su nombre en mayúsculas.\n"
"2. Si quiere su nombre en minúsculas.\n"
"3. Si quiere su nombre con la primera letra mayúscula.\n"))

if opcion == 1:
    print(nombre_usuario_ejercicio8.upper())
if opcion == 2:
    print(nombre_usuario_ejercicio8.lower())
if opcion == 3:
    print(nombre_usuario_ejercicio8.title())

#9) Ejercicio 9

magnitud_del_terremoto = float(input("Ingrese la magnitud del terremoto: "))

if magnitud_del_terremoto < 3:
    print("Muy leve (imperceptible).")
elif magnitud_del_terremoto < 4:
    print("Leve (ligeramente perceptible).")
elif magnitud_del_terremoto < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitud_del_terremoto < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif magnitud_del_terremoto < 7:
    print("Muy Fuerte (puede causar daños significativos).")
else:
    print("Extremo (puede causar graves daños a gran escala).")

#10 Ejercicio 10


hemisferio = input("Introduzca en qué hemisferio se encuentra (N/S): ").casefold()
mes = input("Introduzca el mes actual: ").casefold()
dia = int(input("Introduzca el día del mes: "))


if hemisferio in ['n', 'norte']:
    if (mes == "diciembre" and dia >= 21) or (mes in ["enero", "febrero"]) or (mes == "marzo" and dia <= 20):
        print("Invierno")
    elif (mes == "marzo" and dia >= 21) or (mes in ["abril", "mayo"]) or (mes == "junio" and dia <= 20):
        print("Primavera")
    elif (mes == "junio" and dia >= 21) or (mes in ["julio", "agosto"]) or (mes == "septiembre" and dia <= 20):
        print("Verano")
    elif (mes == "septiembre" and dia >= 21) or (mes in ["octubre", "noviembre"]) or (mes == "diciembre" and dia <= 20):
        print("Otoño")
    else:
        print("Datos incorrectos")


elif hemisferio in ['s', 'sur']:
    if (mes == "diciembre" and dia >= 21) or (mes in ["enero", "febrero"]) or (mes == "marzo" and dia <= 20):
        print("Verano")
    elif (mes == "marzo" and dia >= 21) or (mes in ["abril", "mayo"]) or (mes == "junio" and dia <= 20):
        print("Otoño")
    elif (mes == "junio" and dia >= 21) or (mes in ["julio", "agosto"]) or (mes == "septiembre" and dia <= 20):
        print("Invierno")
    elif (mes == "septiembre" and dia >= 21) or (mes in ["octubre", "noviembre"]) or (mes == "diciembre" and dia <= 20):
        print("Primavera")
    else:
        print("Datos incorrectos")

else:
    print("Hemisferio no válido")

