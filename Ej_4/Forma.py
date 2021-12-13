class Forma:
    def __init__(self, nombre, color, x, y):
        self.nombre = nombre
        self.color = color
        self.punto = Punto(x, y)

    def __str__(self):
        print(self.nombre, self.color, self.punto.x, self.punto.y)

    def moverCentro(self, x, y):
        Punto.x = x
        Punto.y = y

    def get_color(self):
        return self.color

    def set_nombre(self, color):
        self.color = color


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
