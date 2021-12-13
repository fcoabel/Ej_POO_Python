class serie:
    # Valores que se toman por defecto
    TITULO_DEFAULT = "TITULO"
    NTEMPORADAS_DEFAULT = 3
    GENERO_DEFAULT = "COMEDIA"
    ENTREGADO_DEFAULT = False
    CREADOR_DEFAULT = "HOLLYWOOD"

    # Constructor de la serie
    def __init__(self, titulo=None, ntemporadas=None, genero=None, creador=None):
        self.titulo = titulo or serie.TITULO_DEFAULT
        self.nTemporadas = ntemporadas or serie.NTEMPORADAS_DEFAULT
        self.genero = genero or serie.GENERO_DEFAULT
        self.creador = creador or serie.CREADOR_DEFAULT
        self.entregado = serie.ENTREGADO_DEFAULT

    # Metodo para imprimir el objeto de la clase
    def __str__(self):
        print(self.titulo, self.nTemporadas, self.genero, self.creador, self.entregado)

    # Metodo para indicar que se ha entregado la serie
    def entregar(self):
        self.entregado = True

    # Metodos get y set aunque en python no son necesarios
    def get_titulo(self):
        return self.titulo

    def get_nTemporadas(self):
        return self.nTemporadas

    def get_genero(self):
        return self.genero

    def get_creador(self):
        return self.creador

    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_nTemporadas(self, nTemporadas):
        self.nTemporadas = nTemporadas

    def set_genero(self, genero):
        self.genero = genero

    def set_creador(self, creador):
        self.creador = creador
