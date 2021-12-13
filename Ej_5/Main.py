from Empleado import *
from Secretario import Secretario
from Vendedor import cocheEmpresa
from Vendedor import Vendedor
from jefeZona import jefeZona

ListaPersonal = []


def anadirPersonal():
    e = Empleado("NombreE", "ApellidoE", "11111111E", "calle Empleado", 612122233, 1000)
    s = Secretario("NombreS", "ApellidoS", "22222222S", "calle Secreterio", 609566575, 1200, 985657668)
    v = Vendedor("NombreV", "ApellidoV", "33333333V", "calle Vendedor", 657678799, 1200, 675432897, "Area 1", 10)
    jZ = jefeZona("NombreJ", "ApellidoJ", "44444444J", "calle JefeZona", 653421221, 1800)

    ListaPersonal.insert(0, e)
    ListaPersonal.insert(1, s)
    ListaPersonal.insert(2, v)
    ListaPersonal.insert(3, jZ)


def asignarCoches():
    ceV = cocheEmpresa("1111VEN", "Seat", "Ibiza")
    ceJZ = cocheEmpresa("2222CJZ", "VolksWagen", "Passat")

    ListaPersonal[2].cocheEmpresa = ceV
    ListaPersonal[3].cocheEmpresa = ceJZ


def salarios(a, em) -> Empleado:
    em.anios = a
    if isinstance(em, Secretario):
        em.setSalario(em.INCREMENTO)
    elif isinstance(em, Vendedor):
        em.setSalario(em.INCREMENTO)
    elif isinstance(em, jefeZona):
        em.setSalario(em.INCREMENTO)
    else:
        pass


def mostrarLista(lista):
    for i in lista:
        i.__str__()
        if isinstance(i, Vendedor) or isinstance(i, jefeZona):
            print("__Coche Empresa__")
            i.cocheEmpresa.__str__()
        print("\n")


if __name__ == '__main__':
    anadirPersonal()
    asignarCoches()
    salarios(3, ListaPersonal[1])
    salarios(5, ListaPersonal[2])
    salarios(2, ListaPersonal[3])
    mostrarLista(ListaPersonal)
