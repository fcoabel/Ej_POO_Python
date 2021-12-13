from Empleado import *


class Secretario(Empleado):
    def __init__(self, n, a, dni, d, t, s, fax):
        super().__init__(n, a, dni, d, t, s)
        self.despacho = True
        self.fax = fax
        self.INCREMENTO = 5

    def __str__(self):
        if isinstance(self, Secretario):
            print(":---Secretario---:")
        super().__str__()
