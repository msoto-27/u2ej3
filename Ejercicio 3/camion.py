class Camion:
    __id = ''
    __nombre = ''
    __patente = ''
    __marca = ''
    __tara = ''
    def __init__(self, identificacion, nombre, patente, marca, tara):
        self.__id = identificacion
        self.__nombre = nombre
        self.__patente = patente
        self.__marca = marca
        self.__tara = tara
    def getID(self):
        return self.__id
    def getNombre(self):
        return self.__nombre
    def getPatente(self):
        return self.__patente
    def getTara(self):
        return self.__tara