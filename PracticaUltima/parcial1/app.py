from aspirante import Aspirante
from carrera import Carrera
from titulo import Titulo
from inscripcion import Inscripcion
from datetime import date
from datos import *

def menu(): 
    return "\n1 - Nueva Inscripción\n2 - Ver carreras\n3 - Ver inscripciones\n4 - Salir\n"

def nuevaInscripcion():
    seleccion = int(input("Ingrese carrera elegida"))
    for carrera in enumerate(carreras,1):
        print(carrera.nombre)

    carreraElegida = carreras[seleccion - 1]

    nombre = input("ingrese nombre")
    apellido = input("ingrese apellido")
    email = input("ingrese email")
    telefono = input("ingrese telefono")

    aspirante = Aspirante(nombre,apellido,email,telefono)

    seleccionT = int(input("Ingrese titulo elegida"))

    for titulo in enumerate(titulos,1):
        print(titulo.nombre)
    
    tituloElegido = titulos[seleccionT - 1]
    aspirante.add_titulo(tituloElegido)

    inscripcion = Inscripcion(aspirante,carreraElegida )
    inscripciones.append(inscripcion)


while True:
    print(menu())
    opt = input("Ingrese la opción seleccionada: ")
    if opt == "1":
        nuevaInscripcion()
        continue
    if opt == "2":
        carrerasOrdenadas = sorted(carreras, key=lambda x: x.comienzo)
        for carrera in carrerasOrdenadas:
            print(carreras)
      
        continue
    if opt == "3":

        for inscripcion in inscripciones:
            if inscripcion.inscripcion_activa:
                print(inscripcion)
       
       
        continue
    if opt == "4":
        print("Saludos.")
        break
    else:
        print("Ingrese una opcion valida.")