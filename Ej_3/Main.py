from Serie import *
from Videojuegos import *

# Creación de las listas
listaSeries = []
listaVideojuegos = []


# Metodo para crear, entregar y añadir las series a la lista
def crearSeries():
    serie1 = serie()
    serie2 = serie("Serie 2", 5, "Thriller", "Productora 1")
    serie3 = serie("Serie 3", 6, "Comedia", "Productora 2")
    serie4 = serie("Serie 4", 10, "Terror", "Productora 3")
    serie5 = serie("Serie 5", 20, "Ciencia Ficción", "Productora 4")

    serie2.entregar()
    serie4.entregar()

    listaSeries.append(serie1)
    listaSeries.append(serie2)
    listaSeries.append(serie3)
    listaSeries.append(serie4)
    listaSeries.append(serie5)


# Metodo para crear, entregar y añadir a la lista los videojuegos
def crearVideojuegos():
    videojuego1 = videojuego()
    videojuego2 = videojuego("Juego 2", 5, "Shooter", "Activision")
    videojuego3 = videojuego("Juego 3", 3, "Battle Royale", "Ubisoft")
    videojuego4 = videojuego("Juego 4", 2, "Aventura", "SEGA")
    videojuego5 = videojuego("Juego 5", 30, "Arcade", "Sony")

    videojuego5.entregar()
    videojuego3.entregar()
    videojuego1.entregar()

    listaVideojuegos.append(videojuego1)
    listaVideojuegos.append(videojuego2)
    listaVideojuegos.append(videojuego3)
    listaVideojuegos.append(videojuego4)
    listaVideojuegos.append(videojuego5)


# Metodo para contar los elementos entregados de la lista
def contarEntregados(Lista):
    aux1 = 0
    nombre = ""
    entregados = ""
    for i in Lista:
        if i.entregado:
            aux1 += 1
            i.__str__()

        if i in listaSeries:
            nombre = "Series"
            entregados = "entregadas: "
        else:
            nombre = "Videojuegos"
            entregados = "entregados: "

    print("Nº de ", nombre, entregados, aux1)


# Metodo para sacar:
#  - el videojuego con más horas
#  - la serie con más temporadas
def masHoras(Lista):
    if Lista == listaVideojuegos:
        mashoras = max(x.get_horas() for x in Lista)

        for i in Lista:
            if i.get_horas() == mashoras:
                i.__str__()
    else:
        mastemporadas = max(x.get_nTemporadas() for x in Lista)

        for i in Lista:
            if i.get_nTemporadas() == mastemporadas:
                i.__str__()


# Ejecución de todos los metodos
if __name__ == '__main__':
    crearVideojuegos()
    crearSeries()
    print("Series Entregadas: ")
    contarEntregados(listaSeries)
    print("-------------------------")
    print("Videojuegos Entregados: ")
    contarEntregados(listaVideojuegos)
    print("-------------------------")
    print("Videojuego con más horas:")
    masHoras(listaVideojuegos)
    print("-------------------------")
    print("Serie con más temporadas:")
    masHoras(listaSeries)
