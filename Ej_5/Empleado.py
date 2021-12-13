class Empleado:
    def __init__(self, n, a, dni, d, t, s):
        self.nombre = n
        self.apellidos = a
        self.DNI = dni
        self.direccion = d
        self.anios = 0
        self.telefono = t
        self.salario = s
        self.supervisor = ""

    def __str__(self):
        print("Empleado: ", self.nombre, ", ", self.apellidos,
              "\nDNI: ", self.DNI,
              "\nDirección: ", self.direccion,
              "\nTeléfono:", self.telefono,
              "\nSalario: ", self.salario,
              "\nAños en la empresa: ", self.anios,
              "\nSupervisor: ", self.supervisor)

    def setSupervisor(self, supervisor):
        self.supervisor = supervisor

    def setSalario(self, INCREMENTO):
        self.salario = self.salario + ((self.salario * (self.INCREMENTO * self.anios)) / 100)

    def getSalario(self):
        return self.salario

    def getSupervisor(self):
        return self.supervisor

    def setAnios(self, anios):
        self.anios = anios

    def getAnios(self):
        return self.Anios
