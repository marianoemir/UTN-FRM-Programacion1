import math

#1) Ejercicio 1 

print("Hola Mundo!")
print("")

#2) Ejercicio 2

nombre_usuario = input("Ingrese su Nombre porfavor:")
print(f"Hola {nombre_usuario}!")
print("")

#3) Ejercicio 3

nombre_del_usuario = input("¿Podria decirme como se llama? ")
print("")
apellido_del_usuario = input("¿Como es su apellido? ")
print("")
edad_del_usuario = input("¿Cuantos años tiene? ")
print("")
residencia_usuario = input("¿Donde Reside? ")
print("")
print(f"Soy {nombre_del_usuario} {apellido_del_usuario},tengo {edad_del_usuario} años y vivo en {residencia_usuario}")
print("")

#4) Ejercicio 4 

radio_de_circulo = float(input("Introduzca el radio de un círculo:"))
print()

area_del_circulo = math.pi * math.pow(radio_de_circulo, 2)
perimetro_del_circulo = 2 * math.pi * radio_de_circulo

print(f"El área del círculo es:{area_del_circulo:.2f}")
print(f"El perímetro del círculo es:{perimetro_del_circulo:.2f}")
print("")

#5) Ejercicio 5

cantidad_de_segundos = int(input("Introduzca la cantidad de segundos que desea convertir a hora:"))
print("")
print(f"{cantidad_de_segundos} equivale en horas a:{cantidad_de_segundos / 3600}")
print("")

#6) Ejercicio 6

tabla_del_numero_ingresado = int(input("Introduzca el numero del cual desea obtener su tabla de multiplicar:"))
print("")
print(f"{tabla_del_numero_ingresado} x 0 = {tabla_del_numero_ingresado * 0}")
print(f"{tabla_del_numero_ingresado} x 1 = {tabla_del_numero_ingresado * 1}")
print(f"{tabla_del_numero_ingresado} x 2 = {tabla_del_numero_ingresado * 2}")
print(f"{tabla_del_numero_ingresado} x 3 = {tabla_del_numero_ingresado * 3}")
print(f"{tabla_del_numero_ingresado} x 4 = {tabla_del_numero_ingresado * 4}")
print(f"{tabla_del_numero_ingresado} x 5 = {tabla_del_numero_ingresado * 5}")
print(f"{tabla_del_numero_ingresado} x 6 = {tabla_del_numero_ingresado * 6}")
print(f"{tabla_del_numero_ingresado} x 7 = {tabla_del_numero_ingresado * 7}")
print(f"{tabla_del_numero_ingresado} x 8 = {tabla_del_numero_ingresado * 8}")
print(f"{tabla_del_numero_ingresado} x 9 = {tabla_del_numero_ingresado * 9}")
print(f"{tabla_del_numero_ingresado} x 10 = {tabla_del_numero_ingresado * 10}")
print("")

#7) Ejercicio 7

numero1 = int(input("Introduzca el primer numero:"))
numero2 = int(input("Introduzca el segundo numero:"))
print("")
print(f"El resultado de la suma es {numero1} + {numero2} = {numero1 + numero2}")
print(f"El resultado de la division es {numero1} / {numero2} = {numero1 // numero2}")
print(f"El resultado de la multiplicacion es {numero1} * {numero2} = {numero1 * numero2}")
print(f"El resultado de la resta es {numero1} - {numero2} = {numero1 - numero2}")
print("")

#8) Ejercicio 8

peso = float(input("Introduzca su peso corporal:"))
altura = float(input("Introduzca su altura:"))
print(f"Su indice de masa corporal es: {peso / (altura ** 2):.2f}")
print("")

#9) Ejercicio 9

celsius = float(input("introduzca la temperatura en grados Celsius:"))
print(f"El equivalente en Fahrenheit es: {celsius * 9/5 + 32:.2f} ºF")

print("")

#10) Ejercicio 10

numero1_prome = float(input("Introduzca el Primer Numero:"))
numero2_prome = float(input("Introduzca el Segundo Numero:"))
numero3_prome = float(input("Introduzca el Tercer Numero:"))

print(f"El promedio es:{(numero1_prome + numero2_prome + numero3_prome) /3:.2f}")