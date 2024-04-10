from datos import *

def menu(): 
    return "\n1 - Home\n2 - Nueva Lista\n3 - Ver listas\n4 - Salir\n"

    

    print("Se creo la lista exitosamente...")

while True:
    print(menu())
    opt = input("Ingrese la opcion seleccionada: ")
    if opt == "1":

        for video in videos:
            print(video) 
       
        continue
    if opt == "2":

        nuevaLista = input("Ingrese nombre de la lista")
        lista = ListaReproduccion(nuevaLista)

        
        for i, video in enumerate(videos):
            print(f" {i + 1}{video.nombre}")

        eleccionVideo= int(input("elija video"))
        
        videoSeleccionado = videos[eleccionVideo - 1]

        
        lista.add_video(videoSeleccionado)
        listas.append(lista)
        print("listo")
        

       
        continue
    if opt == "3":
        for lista in listas:
            if lista.cantidad_videos != 0:
                print(lista)
           
        
        continue
    if opt == "4":
        print("Gracias por utilizar nuestro sistema.")
        break
    else:
        print("Error, Ingrese una opcion valida...")