from Rectangulo import Rectangulo


class Cuadrado(Rectangulo):
        def __init__(self, nombre, color, x, y, lado):
            self.lado = ladoMayor = ladoMenor = lado
            super().__init__(nombre, color, x, y, ladoMayor, ladoMenor)

        def __str__(self):
            super(Cuadrado, self).__str__()
