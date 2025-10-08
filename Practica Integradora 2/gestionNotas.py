alumnos = {     
    60902: "Rodolfo Fernandez",
    61654: "Luis Gomez",
    61852: "Andrea Pereira",
    61754: "Juan Cruz Gonzales"
}

materias = ["Ciencias", "Historia", "Geografia", "Matematicas", "Fisica"]

notasFinales = []


def pedir_nota():
    while True:
        entrada = input("Ingrese nota (0 a 10): ")

        
        if entrada.strip() == "":
            print("Error: no puede dejar vacío. Intente otra vez.")
            continue

        
        if not (entrada.replace(".", "", 1).isdigit()):
            print("Error: debe ingresar un número válido.")
            continue

        nota = float(entrada)

        if 0 <= nota <= 10:
            return nota
        else:
            print("Error: la nota debe estar entre 0 y 10.")


def cargar_notas(nombre):
    print("\nAlumno:", nombre)
    lista_materias = []
    for materia in materias:
        print("\nMateria:", materia)
        n1 = pedir_nota()
        n2 = pedir_nota()
        final = (n1 + n2) / 2
        lista_materias.append([materia, n1, n2, final])
        print("Nota final:", final)
    return lista_materias


def promedio_alumno(lista_materias):
    suma = 0
    for m in lista_materias:
        suma += m[3]
    return suma / len(lista_materias)


def mejor_materia(lista_materias):
    mejor = lista_materias[0]
    for m in lista_materias:
        if m[3] > mejor[3]:
            mejor = m
    return mejor


def mostrar_materias(lista_materias):
    print("\nMaterias y notas:")
    for m in lista_materias:
        print(m[0], "-> Nota1:", m[1], "Nota2:", m[2], "Final:", m[3])


def main():
    for legajo, nombre in alumnos.items():
        materias_cargadas = cargar_notas(nombre)
        mostrar_materias(materias_cargadas)

        mejor = mejor_materia(materias_cargadas)
        print("\nLa mejor materia fue:", mejor[0], "con", mejor[3])

        prom = promedio_alumno(materias_cargadas)
        print("Promedio general de", nombre, ":", prom)
        notasFinales.append([nombre, prom])

    mejor_prom = max(nf[1] for nf in notasFinales)

    mejores_alumnos = [nf for nf in notasFinales if nf[1] == mejor_prom]

    print("\n=== RESULTADO FINAL ===")
    for nf in notasFinales:
        print(nf[0], "->", nf[1])

    print("\nEl/los mejor(es) promedio(s):")
    for nf in mejores_alumnos:
        print("-", nf[0], "con", nf[1])


main()
