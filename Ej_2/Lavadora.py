from Electrodomestico import *


class lavadora(electrodomestico):
    CARGA_DEFAULT = 5

    def __init__(self, preBas=None, co=None, cons=None, peso=None, carga=None):
        super().__init__(preBas, co, cons, peso)
        self.carga = carga or lavadora.CARGA_DEFAULT

    def get_carga(self):
        return self.carga

    def preciofinal(self):
        precio = 0
        precio = super().preciofinal()
        if self.carga > 30:
            precio = precio + 50
        else:
            pass

        return precio

    def __str__(self):
        super().__str__()
        print(self.carga)
