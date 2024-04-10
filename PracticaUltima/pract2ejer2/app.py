from datos import *

clientes =[]

def eliminar_cliente(numero_cliente):
    for cliente in clientes:
        if numero_cliente == cliente.nro_cliente:
            cliente.eliminar_cliente()
            print(f"Cliente {cliente.nombre_apellido} eliminado exitosamente.")
            return
    print("Cliente no encontrado.")


def reactivar_cliente(numero_cliente):
    for cliente in clientes:
        if numero_cliente == cliente.nro_cliente:
            cliente.reactivar_cliente()
            print(f"Cliente {cliente.nombre_apellido} reactivado exitosamente.")
            return
    print("Cliente no encontrado.")

def registrar_cliente():

    nombre = input("Ingrese Nombre  ")

    print("Paises: ")

    for i, pais in enumerate(paises):
        print(f"{i + 1}-{pais.nombre}") 

    while True:
        seleccionPais = int(input("Seleccione su Pais "))
        if seleccionPais < 1 or seleccionPais > 2:
            print("no valido ")
        else:
            eleccionPais = paises[seleccionPais - 1]
            print(eleccionPais)
            break
            
    for i, provincia in enumerate(eleccionPais.mis_provincias):
        print (f"{i + 1} {provincia.nombre}")
    while True:
        seleccionProvincia = int(input("Seleccione Provincia"))
        if seleccionProvincia <1 or seleccionProvincia > 2:
            print("no valido")
        else:
            eleccionProvincia = provincias[seleccionProvincia - 1]
            print(eleccionProvincia)
            break

    for i, localidad in enumerate(eleccionProvincia.mis_localidades):
        print(f"{i +1 }- {localidad.nombre}")

    while True:
        seleccionLocalidad = int(input("Seleccione localidad"))
        if seleccionLocalidad < 1 or seleccionLocalidad >2:
            print("no valido")
        else:
            eleccionLocalidad = localidades[seleccionLocalidad - 1]
            print(eleccionLocalidad)
            break

    direccion = input("ingrese su direccion")

    datosCliente = (f" Pais {eleccionPais.nombre} Provincia {eleccionProvincia.nombre} Localidad {eleccionLocalidad.nombre} domicilio {direccion}")

    nro_cliente = Cliente.get_nro_cliente()
    clienteRegistrado = Cliente(nombre, datosCliente)
    clientes.append(clienteRegistrado)
    print(clienteRegistrado.nro_cliente)

def menu():
    while True:
        print("1-Modificar direccion")
        print("2-Eliminar cliente")
        print("3-Reactivar cliente")
        opt = input("Ingrese la opción seleccionada: ")
        if opt == "1":

            nombre = input("Ingrese Nombre  ")

            print("Paises: ")

            for i, pais in enumerate(paises):
                print(f"{i + 1}-{pais.nombre}") 

            while True:
                seleccionPais = int(input("Seleccione su Pais "))
                if seleccionPais < 1 or seleccionPais > 2:
                    print("no valido ")
                else:
                    eleccionPais = paises[seleccionPais - 1]
                    print(eleccionPais)
                    break
            
            for i, provincia in enumerate(eleccionPais.mis_provincias):
                print (f"{i + 1} {provincia.nombre}")
            while True:
                seleccionProvincia = int(input("Seleccione Provincia"))
                if seleccionProvincia <1 or seleccionProvincia > 2:
                     print("no valido")
                else:
                    eleccionProvincia = provincias[seleccionProvincia - 1]
                    print(eleccionProvincia)
                    break

            for i, localidad in enumerate(eleccionProvincia.mis_localidades):
                    print(f"{i +1 }- {localidad.nombre}")

            while True:
                seleccionLocalidad = int(input("Seleccione localidad"))
                if seleccionLocalidad < 1 or seleccionLocalidad >2:
                    print("no valido")
                else:
                    eleccionLocalidad = localidades[seleccionLocalidad - 1]
                    print(eleccionLocalidad)
                    break

            direccion = input("ingrese su direccion")

            datosCliente = (f" Pais {eleccionPais.nombre} Provincia {eleccionProvincia.nombre} Localidad {eleccionLocalidad.nombre} domicilio {direccion}")

            clienteRegistrado = Cliente(nombre, datosCliente)
            clientes.append(clienteRegistrado)
            print(clienteRegistrado.nombre_apellido)
            print(clienteRegistrado.direccion)
   

       
            continue
        if opt == "2":
            numero = int(input("Ingrese número de cliente a eliminar: "))
            eliminar_cliente(numero)
               
            

            continue
        if opt == "3":

            numero = int(input("Ingrese número de cliente a REACTIVAR: "))
            reactivar_cliente(numero)


            continue

        

        if opt == "4":
            print("Saludos.")
            break
        else:
            print("Ingrese una opcion valida.")



while True:
    print("1-Registrar cliente")
    print("2-Buscar cliente")
    opt = input("Ingrese la opción seleccionada: ")
    if opt == "1":
        registrar_cliente()
        continue
    if opt == "2":

        numero = int(input("Ingrese numero cliente"))
        cliente_encontrado = False
        for cliente in clientes:
            if numero == cliente.nro_cliente:
                if cliente.fecha_baja:
                    print(f"Cliente {cliente.nombre_apellido} fue dado de baja en la fecha: {cliente.fecha_baja}")
                    menu()

                else:
                    print(cliente.nombre_apellido)
                    menu()
                cliente_encontrado = True
                break
            else:
                print("no encontrado")
        
        continue

    if opt == "3":
        print("Saludos.")
        break
    else:
        print("Ingrese una opcion valida.")