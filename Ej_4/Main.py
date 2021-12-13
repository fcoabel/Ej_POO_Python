from Circulo import *
from Cuadrado import *
from Elipse import *
from Rectangulo import *

listaObjetos = []


def crearAñadir():
    rec = Rectangulo("Rectangulo", "azul", 12, 34, 3, 2)
    cua = Cuadrado("Cuadrado", "rojo", 32, 23, 5)
    eli = Elipse("elipse", "morado", 5, 6, 1, 2)
    cir = Circulo("Circulo", "amarillo", 56, 54, 4, 5)


    listaObjetos.append(rec)
    listaObjetos.append(cua)
    listaObjetos.append(cir)
    listaObjetos.append(eli)


def mostrar(lista):
    for i in lista:
        i.__str__()


def cambiarColor(Lista):
    for i in Lista:
        i.color = "Verde"


def moverPunto(lista):
    for i in lista:
        i.punto.x = 2
        i.punto.y = 2


if __name__ == '__main__':
    crearAñadir()
    mostrar(listaObjetos)
    cambiarColor(listaObjetos)
    print(":---Colores Cambiados---:")
    mostrar(listaObjetos)
    moverPunto(listaObjetos)
    print(":---Punto Cambiado---:")
    mostrar(listaObjetos)


