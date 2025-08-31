#Ejercicio 1

# Uso un for que va desde 0 hasta 100 inclusive (por eso pongo 100+1 en el rango)

for i in range (0,100+1):
    print(i)

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


#Ejercicio 3

numero_uno = int(input("Introduce el Primer Numero:"))
numero_dos = int(input("Introduce el Segundo Numero:"))

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

#Ejercicio 4

suma_2 = 0

numingresado = int(input("Introduce un número (0 para terminar): "))

#Si el usuario ingresa 0 la suma sera 0 y se saltea el bucle de lo contrario suma hasta que el usuario ingrese 0.
while numingresado != 0:
    suma_2 +=numingresado
    numingresado = int(input("Introduce un número (0 para terminar): "))
print(f"El total de la suma es:{suma_2}")

#Ejercicio 5