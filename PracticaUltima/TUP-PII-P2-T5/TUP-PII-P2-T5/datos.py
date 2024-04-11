from cliente import Cliente
from articulo import Articulo
from paquete import Paquete

#inicializo lista vacía de paquetes
paquetes = []

#genero 2 clientes
cliente1 = Cliente("Juan", "Perez", 2000)
cliente2 = Cliente("Marta", "Sanchez", 1000)

#genero articulos
articulos = [
    Articulo("Cerveza Weisse PATAGONIA Botella 730 Cc"),
    Articulo("Vino Blanco Dulce TORO Ttb 1 Ltr"),
    Articulo("Vermouth MARTINI Extra Dry Botella 995 Cc", True) #articulo fragil
]

#genero paquetes
paquetes.append(Paquete(cliente1))
paquetes.append(Paquete(cliente2))
paquetes.append(Paquete(cliente2))

#agrego articulos al paquete 1
paquetes[0].add_articulo(articulos[0])
paquetes[0].add_articulo(articulos[0])
paquetes[0].add_articulo(articulos[0])
paquetes[0].add_articulo(articulos[0])
paquetes[0].add_articulo(articulos[0])
paquetes[0].add_articulo(articulos[0])
#agrego articulos al paquete 2
paquetes[1].add_articulo(articulos[1])
paquetes[1].add_articulo(articulos[1])
paquetes[1].add_articulo(articulos[2])
#agrego articulos al paquete 3
paquetes[2].add_articulo(articulos[2])
paquetes[2].add_articulo(articulos[2])

paquetes[0].despachar_paquete #despachar paquete 1
paquetes[1].despachar_paquete #despachar paquete 2