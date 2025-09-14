import math 

#Funcion del Ejercicio 1
def imprimir_hola_mundo(): 
    print("Hola Mundo!")

#Funcion del Ejercicio 2
def saludar_usuario(nombre): 
    print(f"Hola {nombre}!")

#Funcion del Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia): 
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Funcion del Ejercicio 4
def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

#Funcion del Ejercicio 5
def segundos_a_horas(segundos):
    return segundos / 3600

#Funcion del Ejercicio 6

def tabla_multiplicar(numero):
    for i in range (1,11):
        print(f"{numero} x {i} = {i * numero}")

#Funcion del Ejercicio 7

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    
    if b == 0:
        division = "No se puede dividir por 0"
    else:
        division = a / b
    
    return (suma, resta, multiplicacion, division)


def imprimir_resultados(tupla):
    print(f"El resultado de la suma es: {tupla[0]}")
    print(f"El de la resta es: {tupla[1]}")
    print(f"El de la multiplicación es: {tupla[2]}")
    print(f"El de la división es: {tupla[3]}")

#Funcion del Ejercicio 8

def calcular_imc(peso, altura):
    return peso / (altura * altura)

#Funcion del Ejercicio 9

def celsius_a_fahrenheit(celsius):
    return (1.8 * celsius) + 32

#Funcion del Ejercicio 10

def calcular_promedio(a, b, c):
    return (a + b + c ) / 3

#Programa Principal

#Llamada a la funcion del ejercicio 1 (imprime hola mundo)
imprimir_hola_mundo() 
print("")

#Llamada del ejercicio 2 (Saluda al usuario con su nombre)
saludar_usuario(input("Introduce tu nombre: ")) 
print("")


#Llamada de funcion del Ejercicio 3 (Pide y imprime datos personales)

nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
edad = int(input("Introduce tu edad: "))
residencia = input("Introduce tu residencia: ")

informacion_personal(nombre, apellido, edad , residencia) 

print("")

#Llamada de la funcion del ejercicio 4

entrada_de_radio = float(input("Introduce el radio del circulo: "))

print(f"El área del círculo es: {calcular_area_circulo(entrada_de_radio):.2f}")
print(f"El perímetro del círculo es: {calcular_perimetro_circulo(entrada_de_radio):.2f}")

print("")

#Llamada de la funcion del ejercicio 5

ingreso_de_segundos_usuario = int(input("Ingrese los segundos que quiere convertir en horas: "))

print(f"La cantidad de segundos que usted ingresó: {ingreso_de_segundos_usuario} equivale a {segundos_a_horas(ingreso_de_segundos_usuario):.2f} horas")

print("")

#Llamada a la funcion del ejercicio 6

numero_de_tabla_de_multiplicar = int(input("Ingrese el numero de la tabla de multiplicar que desea obtener: "))

tabla_multiplicar(numero_de_tabla_de_multiplicar)

print("")

#Llamada a la funcion del ejercicio 7

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

resultados = operaciones_basicas(numero1, numero2)
imprimir_resultados(resultados)

#Llamada a la funcion del ejercicio 8

pesodepersona = float(input("Ingrese su peso: "))
alturadelapersona = float(input("Ingrese la altura: "))

print(f"Su indice de masa corporal es: {calcular_imc(pesodepersona, alturadelapersona):.2f}")

print("")

#Llamada de la funcion del ejercicio 9

grados_celsius = float(input("Introduce los grados Celsius que deseas convertir: "))

print(f"{grados_celsius:.2f} °C equivalen a {celsius_a_fahrenheit(grados_celsius):.2f} °F")

#Llamada a la funcion del ejercicio 10

numero1_del_promedio = float(input("Introduce el primer numero: "))
numero2_del_promedio = float(input("Introduce el segundo numero: "))
numero3_del_promedio = float(input("Introduce el tercero numero: "))

print(f"El promedio es: {calcular_promedio(numero1_del_promedio, numero2_del_promedio, numero3_del_promedio):.2f}")