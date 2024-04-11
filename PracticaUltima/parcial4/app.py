from datos import *

def menu(): 
    return "\n1 - Nueva Compra\n2 - Resumen Compras\n3 - Salir\n"

def menu_compra():
    return "\n1 - Agregar Producto\n2 - Finalizar Compra\n"



while True:
    print(menu())
    opt = input("Ingrese la opcion seleccionada: ")
    opt2 = 0
    if opt == "1":


        nueva_compra = Compra(cliente1) 
        compras.append(nueva_compra)

        

        while opt != 2: 

                
                print(menu_compra())   
                opt2 = input("Ingrese una opcion: ")
                if opt2 == "1":
                    for i, producto in enumerate(productos):
                        print(f"{i +1} {producto.codigo} {producto.nombre} {producto.precio_unitario}")
        
                    seleccion = int(input("seleccione producto"))
                    productoSeleccionado = productos[seleccion -1]

                
                    nueva_compra.add_producto(productoSeleccionado)

                
                elif opt2 == "2" :

                    
                    nueva_compra.facturar_compra()
                    

                    break

                    ""
                else:
                    print("Error, Ingrese una opcion valida...")

            
                      
        pass
    elif opt == "2":
        for compra in compras:
            print(f"fecha:{compra.fecha_hora} monto: {compra.monto_facturado} cant productos {compra.cantidad_productos} cliente {compra.cliente.nro_documento}")
        pass
    elif opt == "3":
        print("Gracias por utilizar nuestro sistema.")
        break
    else:
        print("Error, Ingrese una opcion valida...")