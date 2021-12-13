import string

from Electrodomestico import *
from Lavadora import *
from Television import *

if __name__ == '__main__':
    Lista = [electrodomestico(50, "blanco", "A", 20),
             electrodomestico(30, "azul", "d", 40),
             electrodomestico(1, "green", "z"),
             lavadora(50, "negro", "B", 20, 30),
             lavadora(300, "gris", "E", 10),
             lavadora(),
             television(700, "amarillo", "f", 5, 30, True),
             television(50, "rojo", "c", 20, 50, False),
             television(),
             television()]

    for i in Lista:
        i.__str__()
        print("--PRECIO FINAL--: ")
        print(i.preciofinal())
        print("------")
