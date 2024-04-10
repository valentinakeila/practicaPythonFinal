from datos import *

def registrarProfesional():
    nombre = input("Ingrese nombre\n")
    apellido = input("Ingrese apellido\n")
    documento = input("Ingrese documento\n")

    prof = Profesional(nombre, apellido,documento)

    while True:
        for i, titulo in enumerate(titulos):
            print(f"{i +1} {titulo.nombre}")

        seleccion = int(input("Seleccione sus titulos, presione s para salir"))
        tituloSeleccionado = titulos[seleccion -1]
        prof.add_titulos(tituloSeleccionado)
        if seleccion == "s":
            profesionales.append(prof)
            break

def cancelarInscripcion():
    documento = input("ingrese documento")

    profesional_encontrado = False
    for profesional in profesionales:
        if documento == profesional.nro_documento:
            profesional_encontrado = True
            print("Inscripciones del profesional:")
            for concurso in concursos:
                for inscripcion in concurso.mis_incripciones:

                        print(inscripcion)
        
        else:
            print("Profesional no encontrado.")
            break

    # Mostramos todas las inscripciones del profesional
    
   




while True:
    print("1- Nueva inscripcion\n")
    print("2-Cancelar inscripcion\n")
    print("3-Registrar profesional\n")
    opt = input("Ingrese la opción seleccionada: ")
    if opt == "1":
       
        continue
    if opt == "2":
        cancelarInscripcion()
        
        continue
    if opt == "3":
        
        registrarProfesional()
       
        continue
    if opt == "4":
        print("Saludos.")
        break
    else:
        print("Ingrese una opcion valida.")