from datetime import *

class Estadia:
    def __init__(self, nroPatente: str ) -> None:
        self.__fecha = datetime.today()
        self.__nroPatente = nroPatente
        self.__hora_entrada = datetime.now().hour
        self.__hora_salida = None
        self.__estado = "ACTIVO"
        self.__pagado = False
        self.__cantHoras = None


    @property
    def fecha(self):
        return self.__fecha
    
    @fecha.setter
    def fecha(self, nuevaFecha):
        self.__fecha = nuevaFecha

    @property
    def nroPatente(self):
        return self.__nroPatente
    
    @nroPatente.setter
    def nroPatente(self, patente):
        self.__nroPatente = patente

    @property
    def hora_entrada(self):
        return self.__hora_entrada
    

    @hora_entrada.setter
    def hora_entrada(self, hraEntrada):
        self.__hora_entrada = hraEntrada

    @property
    def hora_salida(self):
        return self.__hora_salida

    @hora_salida.setter
    def hora_salida(self, valor):
        self.__hora_salida = valor

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, valor):
        self.__estado = valor

    @property
    def pagado(self):
        return self.__pagado

    @pagado.setter
    def pagado(self, valor):
        self.__pagado = valor

    @property
    def cantHoras(self):
        return self.__cantHoras

    @cantHoras.setter
    def cantHoras(self, valor):
        self.__cantHoras = valor


    def __str__(self) -> str:
      return f" fecha: {self.__fecha} patente: {self.__nroPatente} hora entrada: {self.__hora_entrada} hora salida: {self.__hora_salida}cantidad de horas: {self.__cantHoras} estado: {self.__estado} pagado: {self.__pagado}"
    

    def registrar_salida(self):
        self.__hora_salida = datetime.now().hour
        self.__cantHoras = self.__hora_salida - self.__hora_entrada