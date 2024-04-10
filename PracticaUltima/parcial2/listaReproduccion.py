from video import *
from datetime import *

class  ListaReproduccion:
    prox_nro = int(0)
    def __init__(self, nombre:str) -> None:
        self.__nro = ListaReproduccion.get_prox_nro()
        self.__nombre = nombre
        self.__mis_videos = []


    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre1):
        self.__nombre = nombre1

    @property
    def nro(self):
        return self.__nro
    
    @property
    def mis_videos(self):
        return self.__mis_videos
    
    def add_video(self, video: Video):
        self.__mis_videos.append(video)

    def remove_video(self, video:Video):
        self.__mis_videos.remove(video)

    @property
    def cantidad_videos(self):
        return len(self.__mis_videos)
    
    @classmethod
    def get_prox_nro(cls):
        cls.prox_nro += 1
        return cls.prox_nro
    
    def __str__(self) -> str:
        return f"{self.__nro} {self.__nombre} {self.cantidad_videos}"
    



    
        