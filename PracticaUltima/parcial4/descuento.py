class Descuento:
    descuento_comunidad = 0.20

    @staticmethod
    def pago_con_comunidad(monto:int):
        descuento = Descuento.descuento_comunidad * monto
        total = monto - descuento
        return total
        

        