from pais import Pais
from provincia import Provincia
from localidad import Localidad
from cliente import *



# Lista de países
paises = [
    Pais("Argentina", 1),
    Pais("Brasil", 2),
]

# Lista de provincias
provincias = [
    Provincia("Buenos Aires", 1),
    Provincia("Córdoba", 2),
    Provincia("Río de Janeiro", 3),
    Provincia("São Paulo", 4)
]

# Lista de localidades
localidades = [
    Localidad("Quilmes", 1, 1879),
    Localidad("La Plata", 1, 1900),
    Localidad("Córdoba", 2, 5000),
    Localidad("Villa Carlos Paz", 2, 5152),
    Localidad("Copacabana", 3, 22080),
    Localidad("Ipanema", 3, 22410),
    Localidad("São Paulo", 4, 10000),
    Localidad("Campinas", 4, 13000)
]

# Asignar provincias a cada país
paises[0].mis_provincias = [provincias[0], provincias[1]]  # Argentina
paises[1].mis_provincias = [provincias[2], provincias[3]]  # Brasil

# Asignar localidades a cada provincia
provincias[0].mis_localidades = [localidades[0], localidades[1]]  # Buenos Aires
provincias[1].mis_localidades = [localidades[2], localidades[3]]  # Córdoba
provincias[2].mis_localidades = [localidades[4], localidades[5]]  # Río de Janeiro
provincias[3].mis_localidades = [localidades[6], localidades[7]]  # São Paulo


"""""
cliente_precargado = Cliente("Juan Pérez", "Av. Rivadavia 123")

# Asignar país, provincia y localidad al cliente
cliente_precargado.pais = paises[0]  # Selecciona el primer país en la lista
cliente_precargado.provincia = paises[0].mis_provincias[0]  # Selecciona la primera provincia del primer país
cliente_precargado.localidad = paises[0].mis_provincias[0].mis_localidades[0]  # Selecciona la primera localidad de la primera provincia del primer país

# Agregar el cliente precargado a una lista de clientes
clientes = [cliente_precargado] 
"""
