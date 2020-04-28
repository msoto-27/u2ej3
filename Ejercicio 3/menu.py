import csv

from camion import Camion

from cosecha import Cosecha

def salir():
    pass

def mostrarCamion():
    nc = int(input('Ingrese un ID de camion: '))
    print('El camion', nc, 'ha descargado', cosecha.sumarFila(nc-1),'kilos en total')

def mostrarListado():
    print('PATENTE           CONDUCTOR  CANTIDAD DE KILOS')
    for i in lista_camiones:
        print('%6s %20s %18d' %(i.getPatente(), i.getNombre(), cosecha.sumarFila(i.getID()-1)))

switcher = {
    0: salir,
    1: mostrarCamion,
    2: mostrarListado
}

def switch(arg):
    func = switcher.get(arg, lambda: print("Opción no válida"))
    func()

def cargarCamiones(lista):
    file_camiones = open('camiones.csv')
    reader = csv.reader(file_camiones, delimiter = ',')
    for fila in reader:
        lista_camiones.append(Camion(int(fila[0]), fila[1], fila[2], fila[3], float(fila[4])))
    file_camiones.close()

def cargarCosecha(lista, c):
    file_cosecha = open('cosecha.csv')
    reader = csv.reader(file_cosecha, delimiter = ',')
    for fila in reader:
        camion = int(fila[0]) - 1
        dia = int(fila[1]) - 1
        kilos = float(fila[2]) - lista[camion].getTara()
        c.cargar(camion, dia, kilos)
    #c.mostrar()

if __name__ == '__main__':
    lista_camiones = []
    
    cargarCamiones(lista_camiones)
    cantidad_camiones = len(lista_camiones)
    cosecha = Cosecha(cantidad_camiones)
    cargarCosecha(lista_camiones, cosecha)
    bandera = False
    while not bandera:
        print("""
              0 Salir
              1 Mostrar cantidad descargada por un camion en especifico
              2 Mostrar listado""")
        opcion = int(input("Ingrese una opción: "))
        switch(opcion)
        bandera = int(opcion)==0 