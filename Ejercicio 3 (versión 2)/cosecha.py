class Cosecha:
    __columnas = 45
    __matriz = []
    def __init__(self, filas): #La cantidad de filas esta dada por la cantidad de camiones
        self.__matriz = [[0 for x in range(self.__columnas)] for y in range(0,filas)]
    def cargar(self, fila, columna, valor):
        self.__matriz[fila][columna] += valor
    def mostrar(self):
        print(self.__matriz)
    def sumarFila(self, fila):
        s = 0
        for i in self.__matriz[fila]:
            s += i
        return s
    def getValor(self, fila, columna):
        return self.__matriz[fila][columna]
