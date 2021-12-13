import keyword


class electrodomestico:
    # Declaración de constantes
    PRECIO_BASE_DEFAULT = 100
    COLOR_DEFAULT: str = "Blanco"
    CONSUMO_DEFAULT: str = "F"
    PESO_DEFAULT = 5

    # Declaración de Tuplas y un Diccionario para calcular precion final
    COLORES_DISPONIBLES = ("blanco", "negro", "rojo", "azul", "gris")
    LETRA_CONSUMO = ("A", "B", "C", "D", "E", "F")
    DIC_LETRAPRECIO = {"A": 100, "B": 80, "C": 60, "D": 50, "E": 30, "F": 10}

    # Metodos de la clase
    def __init__(self, preciobase=None, color: str = None, consumo: str = None, peso=None):
        self.preciobase = preciobase or electrodomestico.PRECIO_BASE_DEFAULT
        electrodomestico.__comprobarColor(self, color or electrodomestico.COLOR_DEFAULT)
        electrodomestico.__comprobarConsumo(self, consumo or electrodomestico.CONSUMO_DEFAULT)
        self.peso = peso or electrodomestico.PESO_DEFAULT

    def __comprobarConsumo(self, consumo):
        con = consumo.upper()
        if con in electrodomestico.LETRA_CONSUMO:
            electrodomestico.set_consumo(self, con)
        else:
            electrodomestico.set_consumo(self, electrodomestico.CONSUMO_DEFAULT)

    def __comprobarColor(self, co):
        co = co.lower()
        if co in electrodomestico.COLORES_DISPONIBLES:
            electrodomestico.set_color(self, co)
        else:
            self.color = electrodomestico.COLOR_DEFAULT

    def preciofinal(self):
        precio = 0
        if self.consumo in electrodomestico.DIC_LETRAPRECIO:
            precio = self.preciobase + electrodomestico.DIC_LETRAPRECIO[self.consumo]
            pass

        if 0 < self.peso <= 19:
            precio = precio + 10
        elif 20 <= self.peso <= 49:
            precio = precio + 50
        elif 50 <= self.peso <= 79:
            precio = precio + 80
        elif self.peso > 80:
            precio = precio + 100

        return precio

    def get_preciobase(self):
        return self.preciobase

    def get_color(self):
        return self.color

    def get_consumo(self):
        return self.consumo

    def get_peso(self):
        return self.peso

    def set_preciobase(self, preciobase):
        self.preciobase = preciobase

    def set_color(self, color):
        self.color = color

    def set_consumo(self, consumo):
        self.consumo = consumo

    def set_peso(self, peso):
        self.peso = peso

    def __str__(self):
        print(self.preciobase, self.color, self.consumo, self.peso)
