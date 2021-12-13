from Forma import *


class Rectangulo(Forma):
    def __init__(self, nombre, color, x, y, ladoMayor, ladoMenor):
        super().__init__(nombre, color, x, y)
        self.ladoMayor = ladoMayor
        self.ladoMenor = ladoMenor

    def __str__(self):
        super().__str__()

    def calcularArea(self):
        area = self.ladoMayor * self.ladoMenor
        return area

    def calcularPerimetro(self):
        perimetro = (self.ladoMenor * 2) + (self.ladoMayor * 2)
        return perimetro

    def cambiarTamaño(self, escala):
        self.ladoMenor = self.ladoMenor * escala
        self.ladoMayor = self.ladoMayor * escala
