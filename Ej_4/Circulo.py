from Elipse import Elipse
from math import sqrt
import math


class Circulo(Elipse):
    def __init__(self, nombre, color,  x, y, r, R):
        super().__init__(nombre, color, x, y, r, R)
        self.radio = r - R

    def __str__(self):
        super(Circulo, self).__str__()

    def area(self):
        area = math.pi * sqrt(self.radio)
        return area
