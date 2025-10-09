
def leer_alumnos():
    alumnos = []
    try:
        with open("alumnos.txt", "r", encoding="utf-8") as f:
            for linea in f:
                partes = linea.strip().split(";")
                if len(partes) == 4:
                    nombre, apellido, legajo, nota = partes
                    alumnos.append({
                        "nombre": nombre,
                        "apellido": apellido,
                        "legajo": legajo,
                        "nota": float(nota)
                    })
    except FileNotFoundError:
        with open("alumnos.txt", "w", encoding="utf-8") as f:
            pass
    except Exception as e:
        print("Error al leer el archivo:", e)
    return alumnos


def mostrar_alumnos(alumnos):
    if not alumnos:
        print("No hay alumnos cargados.")
    else:
        for a in alumnos:
            print(f"{a['nombre']} {a['apellido']} - Legajo: {a['legajo']} - Nota: {a['nota']}")


def validar_existe_alumno(diccionario, legajo):
    return legajo in diccionario


def agregar_alumno(alumnos, diccionario):
    print("---- Agregar Alumno ----")

    nombre = input("Nombre: ").strip()
    if not nombre.isalpha():
        print("El nombre solo puede tener letras.")
        return

    apellido = input("Apellido: ").strip()
    if not apellido.isalpha():
        print("El apellido solo puede tener letras.")
        return

    legajo = input("Legajo (5 dígitos): ").strip()
    if not (legajo.isdigit() and len(legajo) == 5):
        print("El legajo debe tener 5 números.")
        return

    if validar_existe_alumno(diccionario, legajo):
        print(f"El legajo {legajo} ya existe en el archivo alumnos.txt, no se permite su escritura.")
        return

    nota_str = input("Nota promedio (1 a 10): ").strip()
    if not nota_str.replace(".", "", 1).isdigit():
        print("La nota debe ser un número.")
        return

    nota = float(nota_str)
    if nota < 1 or nota > 10:
        print("La nota debe estar entre 1 y 10.")
        return

    alumno = {"nombre": nombre, "apellido": apellido, "legajo": legajo, "nota": nota}
    alumnos.append(alumno)
    diccionario[legajo] = alumno

    try:
        with open("alumnos.txt", "a", encoding="utf-8") as f:
            f.write(f"{nombre};{apellido};{legajo};{nota}\n")
        print("Alumno agregado correctamente.")
    except Exception as e:
        print("Error al escribir el archivo:", e)


def guardar_aprobados(alumnos):
    aprobados = [a for a in alumnos if a["nota"] >= 6]
    try:
        with open("aprobados.txt", "w", encoding="utf-8") as f:
            for a in aprobados:
                f.write(f"{a['nombre']};{a['apellido']};{a['legajo']};{a['nota']}\n")
        print("---- Alumnos Aprobados ----")
        for a in aprobados:
            print(f"{a['nombre']} {a['apellido']} - Nota: {a['nota']}")
    except Exception as e:
        print("Error al crear aprobados.txt:", e)



def main():
    alumnos = leer_alumnos()
    diccionario = {a["legajo"]: a for a in alumnos}

    while True:
        print("\n--- MENÚ ---")
        print("1. Ver alumnos")
        print("2. Agregar alumno")
        print("3. Generar y mostrar archivo de aprobados")
        print("4. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            mostrar_alumnos(alumnos)
        elif opcion == "2":
            agregar_alumno(alumnos, diccionario)
        elif opcion == "3":
            guardar_aprobados(alumnos)
        elif opcion == "4":
            print("Fin del programa.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
