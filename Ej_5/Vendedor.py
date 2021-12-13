from Empleado import *


class Vendedor(Empleado):
    ListaClientes = []

    def __init__(self, n, a, dni, d, t, s, mE, areaVenta, comisiones):
        super().__init__(n, a, dni, d, t, s)
        self.cocheEmpresa = None
        self.movilEmpresa = mE
        self.areaVenta = areaVenta
        self.comisiones = comisiones
        self.INCREMENTO = 10

    def __str__(self):
        if isinstance(self, Vendedor):
            print(":---Vendedor---:")
        super().__str__()

    def altaCliente(self, cliente):
        self.ListaClientes.append(cliente)

    def bajaCliente(self, cliente):
        self.ListaClientes.remove(cliente)

    def cambiarCoche(self, matricula, marca, modelo):
        self.cocheEmpresa = cocheEmpresa(matricula, marca, modelo)


class cocheEmpresa():
    def __init__(self, matricula, marca, modelo):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        print("Matricula: ", self.matricula,
              "\nMarca: ", self.marca,
              "\nModelo: ", self.modelo)
