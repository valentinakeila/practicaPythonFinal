from datos import *

def menu(): 
    return "\n1 - Nueva Carpeta\n2 - Seleccionar Carpeta\n3 - Papelera\n4 - Salir"

def menu_carpeta():
    return "\n1 - Eliminar Carpeta\n2 - Volver"

while True:

    print(menu())
    opt = input("Ingrese la opcion seleccionada: ")
    
    if opt == "1":
        pass
        print("Creación exitosa")
    
    elif opt == "2":
        pass

    elif opt == "3":
        pass

    elif opt == "4":
        print("Gracias por utilizar nuestro sistema.")
        break
    else:
        print("Error, Ingrese una opcion valida...")