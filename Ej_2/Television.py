from Electrodomestico import *


class television(electrodomestico):
    RESOLUCION_DEFAULT = 20
    FOURK_DEFAULT = False

    def __init__(self, preBas=None, co=None, con=None, peso=None, resolucion = None, fourK = None):
        super().__init__(preBas, co, con, peso)
        self.resolucion = resolucion or television.RESOLUCION_DEFAULT
        self.fourK = fourK or television.FOURK_DEFAULT

    def preciofinal(self):
        precio = 0
        precio = super(television, self).preciofinal()

        if self.resolucion > 40:
            precio = (precio * 30)/100
        else:
            pass

        if self.fourK:
            precio = precio + 50
        else:
            pass

        return print(precio)

    def get_resolucion(self):
        return self.resolucion

    def get_fourK(self):
        return self.fourK

    def __str__(self):
        super().__str__()
        print(self.resolucion, self.fourK)