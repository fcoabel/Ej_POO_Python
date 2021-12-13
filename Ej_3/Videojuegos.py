class videojuego:
    # Valores que se toman por defecto
    ENTREGADO_DEFAULT = False
    HORAS_DEFAULT = 10
    TITULO_DEFAULT = "TITULO"
    GENERO_DEFAULT = "GENERO"
    COMPANIA_DEFAULT = "COMPAÑIA"

    # Constructor del videojuego
    def __init__(self, titulo=None, horas=None, genero=None, compania=None):
        self.titulo = titulo or videojuego.TITULO_DEFAULT
        self.horas = horas or videojuego.HORAS_DEFAULT
        self.genero = genero or videojuego.GENERO_DEFAULT
        self.compania = compania or videojuego.COMPANIA_DEFAULT
        self.entregado = videojuego.ENTREGADO_DEFAULT

    # Metodo para imprimir el objeto de la clase
    def __str__(self):
        print(self.titulo, self.horas, self.genero, self.compania, self.entregado)

    # Metodo para indicar que se ha entregado el videojuego
    def entregar(self):
        self.entregado = True

    # Metodos get y set de las variables aunque en python no son necesarias
    def get_titulo(self):
        return self.titulo

    def get_horas(self):
        return self.horas

    def get_genero(self):
        return self.genero

    def get_compania(self):
        return self.compania

    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_horas(self, horas):
        self.horas = horas

    def set_genero(self, genero):
        self.genero = genero

    def set_compania(self, compania):
        self.compania = compania
