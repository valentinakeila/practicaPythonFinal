class Precio:
    precio = 100

    @staticmethod
    def calcular_importe(cant_horas: int):
        return Precio.precio * cant_horas