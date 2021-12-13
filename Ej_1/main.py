from Persona import *

listaPersonas = []


def pedirDatos():

    nombre = input("Introduce el Nombre: ")
    apellidos = input("Introduce el Apellido: ")
    edad = input("Introduce la Edad: ")
    sexo = input("Introduce el Sexo: ")
    peso = input("Introduce el Peso: ")
    altura = input("Introduce la Altura: ")

    persona1 = Persona(nombre, apellidos, edad, sexo, peso, altura)
    persona2 = Persona(nombre, apellidos, edad, sexo)
    persona3 = Persona()

    listaPersonas.append(persona1)
    listaPersonas.append(persona2)
    listaPersonas.append(persona3)


def mostrarDatos(lista):
    for i in lista:
        print(i.calcularIMC(Persona.get_peso(i), Persona.get_altura(i)))
        print(i.esMayorDeEdad(Persona.get_edad(i)))
        i.__str__()



if __name__ == '__main__':
    pedirDatos()
    mostrarDatos(listaPersonas)

