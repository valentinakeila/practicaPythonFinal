from datos import *

def menu(): 
    return "\n1 - Comenzar a preparar paquete\n2 - Paquetes preparados\n3 - Salir\n"

def menu_paquete():
    return "\n1 - Agregar Producto\n2 - Finalizar preparado y despachar\n"

def cliente_paquete():
    '''
        dummy function
        retorna cliente al que se le prepara el paquete
    '''
    return cliente1

while True:
    print(menu())
    opt = input("Ingrese la opcion seleccionada: ")
    if opt == "1":
        nuevo_paquete = Paquete(cliente_paquete())
        paquetes.append(nuevo_paquete) #se genera un nuevo paquete con el cliente 
        while True:
            print(menu_paquete())
            opt = input("Ingrese la opcion seleccionada: ")
            if opt == "1":

                for i, producto in enumerate(articulos):
                    print(f"{i + 1} {producto.codigo} {producto.descripcion}")

                seleccion = int(input("Ingrese articulo"))
                articuloSeleccionado = articulos[seleccion - 1]

    
                nuevo_paquete.add_articulo(articuloSeleccionado)

                pass
            elif opt == "2" :
                nuevo_paquete.despachar_paquete
                
                pass
                break
            else:
                print("Error, Ingrese una opcion valida...")
    elif opt == "2":
        for despachado in paquetes:
            print(f"paquete para: {despachado.cliente.nombre}{despachado.apellido} [Despachado {despachado.paquete_despachado}] tiempo preparacion: {despachado.tiempo_preparacion} fragiles: {despachado.cantidad_articulos_fragiles}" )
        pass
    elif opt == "3":
        print("Gracias por utilizar nuestro sistema.")
        break
    else:
        print("Error, Ingrese una opcion valida...")