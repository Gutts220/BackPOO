import time
import datetime

class registro:
    __fecha: datetime
    __hora_entrada: time
    __hora_salida: time
    __dependencia: str
    def __init__(self, fecha, hora_entrada, hora_salida, dependencia):
        self.__fecha = fecha
        self.__hora_entrada = hora_salida
        self.__hora_salida = hora_entrada
        self.__dependencia = dependencia
    def get_fecha(self):
        return self.__fecha
    def get_hora_entrada(self):
        return self.__hora_entrada
    def get_hora_salida(self):
        return self.__hora_salida
    def obt_dependencia(self):
        return self.__dependencia