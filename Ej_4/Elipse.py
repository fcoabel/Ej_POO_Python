from Forma import *
import math


class Elipse(Forma):

    def __init__(self, nombre, color, x, y, r, R):
        super().__init__(nombre, color, x, y)
        self.r = r
        self.R = R

    def areaElipse(self):
        area = math.pi * (self.R * self.r)
        return area
