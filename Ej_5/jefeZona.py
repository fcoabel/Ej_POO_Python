from Empleado import *
from Secretario import Secretario
from Vendedor import cocheEmpresa
from Vendedor import Vendedor


class jefeZona(Empleado):
    listaVendedores = []

    def __init__(self, n, a, dni, d, t, s):
        super().__init__(n, a, dni, d, t, s)
        self.despacho = True
        self.secretario = None
        self.cocheEmpresa = None
        self.INCREMENTO = 20

    def __str__(self):
        if isinstance(self, jefeZona):
            print(":---Jefe De Zona---:")
        super().__str__()

    def setSecretario(self, n, a, dni, d, t, s):
        self.secretario = Secretario(n, a, dni, d, t, s)

    def setCoche(self, matricula, marca, modelo):
        self.cocheEmpresa = cocheEmpresa(matricula, marca, modelo)

    def setVendedor(self, n, a, dni, d ,t, s, mE, areaVenta, comisiones):
        v = Vendedor(n, a, dni, d, t, s, mE, areaVenta, comisiones)
        self.listaVendedores.append(v)

    def removeVendedor(self, x):
        self.listaVendedores.remove(x)
