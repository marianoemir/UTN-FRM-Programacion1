import random 

#Ejercicio 1

# Uso un for que va desde 0 hasta 100 inclusive (por eso pongo 100+1 en el rango)

for k in range (0,100+1):
    print(k)
print("")

#Ejercicio 2

numero_del_usuario = int(input("Introduce un número: "))
contador = 0
copia_de_num_usuario = numero_del_usuario

# Caso especial: 0 tiene 1 dígito
if numero_del_usuario == 0:
    contador += 1

# Usamos el valor absoluto para contar dígitos, pero guardamos el original para mostrarlo
num = abs(numero_del_usuario)
while num > 0:
    num = num // 10
    contador += 1

print(f"La cantidad de dígitos del número {copia_de_num_usuario} es: {contador}")
print("")

#Ejercicio 3

numero_uno = int(input("Introduce el Primer Numero: "))
numero_dos = int(input("Introduce el Segundo Numero: "))

variable_de_seguridad1 = 0
variable_de_seguridad2 = 0
suma = 0

#Este if y las variables de seguridad tienen el proposito de identificar al numero mayor que ingrese el usuario.
if numero_uno > numero_dos:
    variable_de_seguridad1 = numero_uno
    variable_de_seguridad2 = numero_dos
elif numero_dos > numero_uno:
    variable_de_seguridad1 = numero_dos
    variable_de_seguridad2 = numero_uno

else:
    variable_de_seguridad1 = numero_uno
    variable_de_seguridad2 = numero_dos

"""El enunciado me pide que excluya a los numeros que ingreso el usuario entonces agrego un +1 en el menor y 
el ultimo numero excluido por el bucle"""
for i in range(variable_de_seguridad2 + 1, variable_de_seguridad1):
    suma += i

print(f"La suma de los números comprendidos entre {variable_de_seguridad2} y {variable_de_seguridad1} es: {suma}")
print("")

#Ejercicio 4

suma_2 = 0

numingresado = int(input("Introduce un número (0 para terminar): "))

#Si el usuario ingresa 0 la suma sera 0 y se saltea el bucle de lo contrario suma hasta que el usuario ingrese 0.
while numingresado != 0:
    suma_2 +=numingresado
    numingresado = int(input("Introduce un número (0 para terminar): "))
print(f"El total de la suma es:{suma_2}")
print("")

#Ejercicio 5

#Importe la libreria random para poder generar un numero aleatorio.
numero_aleatorio = random.randint(0,9)
contador2 = 0

#El programa se ejecuta si o si y cuando acertamos se corta y muestra el numero de intentos.
while True:
    eluseradivina = int(input("Debe adivinar un numero del 0 al 9: "))
    contador2 += 1
    if(eluseradivina == numero_aleatorio):
        break
print(f"Felicidades adivino el numero le costo {contador2} intentos.")
print("")

#Ejercicio 6

"""Bucle que muestra los numeros pares de 0 a 100 de manera decreciente cabe recalcar el -1 del segundo 
Argumento del for es para que imprima 0 tambien"""
for j in range (100 , -1, -1):
    if(j % 2 == 0):
        print(j)

print("")

#Ejercicio 7

#Con la funcion abs transformo el numero del usuario a numero positivo si es que ingresa algo negativo
numerito_pedidoaluser = abs(int(input("Introduce el numero: ")))
suma3 = 0

for g in range (0,numerito_pedidoaluser +1):
    suma3 += g

print(f"La suma de todos los numeros comprendidos entre 0 y {numerito_pedidoaluser} es:{suma3}")

print("")

#Ejercicio 8

numeros_pares = 0
numeros_impares = 0
numeros_positivos = 0
numeros_negativos = 0

numero_del_usuario = 0

#El bucle pregunta 100 numeros al usuario y los contadores clasifican lo que ingreso el usuario si es par o impar positivo o negativo.
for cienvari in range(100): 
    numero_del_usuario = int(input(f"Introduce 100 números (Le quedan {100 - cienvari}): "))
    if numero_del_usuario % 2 == 0:
        numeros_pares += 1
    elif numero_del_usuario % 2 != 0:
        numeros_impares += 1
    
    if numero_del_usuario > 0:
        numeros_positivos += 1
    elif numero_del_usuario < 0:
        numeros_negativos += 1

print(f"De los 100 numeros que usted ingreso la cantidad de pares son: {numeros_pares} , la cantidad de impares son: {numeros_impares} \n la cantidad de positivos son: {numeros_positivos} y de negativos son {numeros_negativos}.")

print("")

#Ejercicio 9
lo_que_ingresa_el_usuario = 0
suma_promedo_de_ciennumeros = 0
media_de_ciennumeros = 0

#El usuario ingresa 100 numeros se suman en el bucle despues del bucle esa suma se divide entre 100 para saber la media.
for cien_promedio in range (100):
    lo_que_ingresa_el_usuario = int(input(f"Ingrese 100 numeros para saber su media (Le quedan {100 - cien_promedio}): "))
    suma_promedo_de_ciennumeros += lo_que_ingresa_el_usuario

media_de_ciennumeros = suma_promedo_de_ciennumeros /100

print(f"La media de los 100 numeros es:{media_de_ciennumeros}")

print("")

#Ejercicio 10
numero_ainvertir = int(input("Ingrese el numero que quiere invertir: "))

#Guarda el signo en caso de que el numero sea negativo.
signo = -1 if numero_ainvertir < 0 else 1  
abs_num = abs(numero_ainvertir)  #Lo transformo en positivo.      
str_num = str(abs_num)         #Lo transformo a cadena.
invertido_str = str_num[::-1]  #Lo invierto con propiedades de string.
invertido_int = int(invertido_str) #Lo vuelvo a transformar en entero.
numero_invertido = invertido_int * signo  #aplicamos el signo correcto.

print("El numero invertido es:", numero_invertido)
