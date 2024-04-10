
from estadia import *
from precio import *

estadias = [Estadia("0000")]


def ingreso():
    patente = input("Ingrese patente")
    for estadia in estadias:
        if estadia.nroPatente == patente:
            print(" patente ya registrada")

        else:
            estadia = Estadia(patente)
            estadias.append(estadia)
            print("registrado")
            break


def egreso():
    patente = input("Ingrese patente")
    for estadia in estadias:
        if estadia.nroPatente == patente:
             estadia.registrar_salida()
             importe = Precio.calcular_importe(estadia.cantHoras) # estadia se convirtio en objeto por el for con cantHoras estas accediendo al atributo de la clase Estadia
             print(f"El precio a pagar es ${importe}")
             confirmacion = input("¿Desea confirmar el pago? (s/n): ")
             if confirmacion.lower() == "s":
                    estadia.pagado = True
                    estadia.estado = "PAGADO"
                    estadia.hora_salida = datetime.now().hour
                    print("El pago ha sido confirmado.")
                    print(estadia)
        else:
           
            print("no encontrado")
            break




opcion = 0
while opcion != 3:
    print("Menú:")
    print("1. Ingresar Estadia")
    print("2. Finalizar Estadia")
    print("3. Salir")
    opcion = input("ingrese opcion")

    if opcion == "1":
        ingreso()

    elif opcion == "2":

        egreso()

    elif opcion == "3":

        print("saludos!")

        break

    else: 
        print("opcion no valida")