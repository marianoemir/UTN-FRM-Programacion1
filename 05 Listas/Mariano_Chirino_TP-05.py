#Ejercicio 1
print("")

multiplode4 = list(range(4,101,4))

print(multiplode4)

print("")

#Ejercicio 2

lista_penultimo = [3.2, 9, True, "Hola", ["Hello", False]]
print(lista_penultimo[-2]) 

print("")


#Ejercico 3

lista_vacia = []

lista_vacia.append("Naranja")
lista_vacia.append("Manzana")
lista_vacia.append("Banana")

print(lista_vacia)

print("")


#Ejercico 4

animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[3] = "oso"

print(animales)

print("")


#Ejercicio 5

#Este programa consiste en eliminar el numero mayor de la lista.

numeros = [8, 15, 3, 22, 7]

#Max devuelve el numero mas grande de la lista y remove lo elimina.
#En el caso de que el numero mas grande se repita se elimina solo su primera aparicion.

numeros.remove(max(numeros))
print(numeros)

print("")


#Ejercicio 6

numerosdel10al30 = list(range(10, 31, 5))

print(numerosdel10al30[0], numerosdel10al30[1])

print()

#Ejercicio 7

autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "amarok"
autos[2] = "bora"

print(autos)

#Ejercicio 8

dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(dobles)

print("")

#Ejercicio 9

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(compras)

print("")

#Ejercicio 10

lista_anidada = [15 ,True, [25.5, 57.9, 30.6], False]

print(lista_anidada)
