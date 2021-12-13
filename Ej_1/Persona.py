import random


class Persona:
    __nombre = "nDefecto"
    __apellidos = "aDefecto"
    __edad = 1
    __sexo = "M"
    __peso = 70
    __altura = 170

    def __init__(self, nombre=None, apellidos=None, edad=None, sexo=None, peso=None, altura=None):
        self.dni = Persona.generarDNI()
        self.nombre = nombre or Persona.__nombre
        self.apellidos = apellidos or Persona.__apellidos
        self.edad = edad or Persona.__edad
        self.sexo = sexo or Persona.__sexo
        self.peso = peso or Persona.__peso
        self.altura = altura or Persona.__altura

    def __str__(self):
        print(self.nombre,
              self.apellidos,
              self.dni,
              self.edad,
              self.sexo,
              self.peso,
              self.altura)

    @staticmethod
    def calcularIMC(peso, altura):

        imc = (int(peso) / (pow(int(altura) / 100, 2)))

        pesoideal = 18.5
        pesosuperior = 24.9

        if pesoideal <= imc < pesosuperior:
            return 0, round(imc, 2)
        elif imc < pesoideal:
            return -1, round(imc, 2)
        elif imc > pesosuperior:
            return 1, round(imc, 2)

    @staticmethod
    def esMayorDeEdad(edad):
        if int(edad) > 18:
            em = True
            return "¿Es Mayor de edad?. " + str(em)
        else:
            em = False
            return "¿Es Mayor de edad?. " + str(em)

    def __introducirSexo(self, sexo):
        if sexo.upper() != "M":
            self.sexo = "M"

    @staticmethod
    def generarDNI():
        randomdni = random.randint(1, 99999999)

        i = randomdni % 23
        letradni = (
            "T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C",
            "K",
            "E")
        dni = str(randomdni) + letradni[i]

        return dni

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellidos(self, apellidos):
        self.apellidos = apellidos

    def set_edad(self, edad):
        self.edad = edad

    def set_altura(self, altura):
        self.altura = altura

    def set_peso(self, peso):
        self.peso = peso

    def set_sexo(self, sexo):
        self.sexo = sexo

    def get_nombre(self):
        return self.nombre

    def get_apellidos(self):
        return self.apellidos

    def get_edad(self):
        return self.edad

    def get_altura(self):
        return self.altura

    def get_peso(self):
        return self.peso

    def get_sexo(self):
        return self.sexo
