from datos import *

def menu(): 
    return "\n1 - Pagina principal\n2 - Nueva Lista de lectura\n3 - Ver listas de lectura\n4 - Salir\n"


    

    print("Se creo la lista exitosamente...")

while True:
    print(menu())
    opt = input("Ingrese la opcion seleccionada: ")
    if opt == "1":

        for libro in sorted(libros, key=lambda x: x.nombre):
            print(libro)
        
        continue
    if opt == "2":
        nombre = input("Ingrese el nombre de la lista: ")
        codigo = int(input("Ingrese el código de la lista: "))
        try:
            lista = ListaLectura(nombre, codigo)
            print("Se creó la lista exitosamente...")
        except Exception as e:
            print(e)

        
        for i, libros in enumerate(libros):
            print(f"{i + 1} {libro.nombre}")

        seleccion = int(input("seleccione libro"))
        libroSeleccionado = libros[seleccion -1]

        listas.add_libro(libroSeleccionado)
        listas.append(lista)

        



        continue
    if opt == "3": 
        for lista in listas:
            print(lista)
        continue
    if opt == "4":
        print("Gracias por utilizar nuestro sistema.")
        break
    else:
        print("Error, Ingrese una opcion valida...")

