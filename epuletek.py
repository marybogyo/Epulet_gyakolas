from Epulet import Epulet
eplulet_lista = []
def beolvas():
    fajl = open("epulet.txt", "r", encoding="utf-8")
    fajl.readline()
    sorok = fajl.readlines()
    fajl.close()
    #print(sorork)

    i = 0
    while i < len(sorok):
        sor = sorok[i].strip().split("$")
        eplulet_lista.append(Epulet(sor))
        i += 1
        #print(sor)


def epluet_szam():
   return len(eplulet_lista)

def magasabb_epulet():
    i = 0
    legm_darab = 0
    while i < len(eplulet_lista):
        if (eplulet_lista[i].getmagassag() * 3.280839895) > 555:
            legm_darab += 1
        i += 1
    return legm_darab

def legoregebb_epulet():
    i = 0
    oregebb = 0
    while i < len(eplulet_lista):
        if eplulet_lista[oregebb].epult > eplulet_lista[i].epult:
            oregebb = i
        i += 1
    return eplulet_lista[oregebb].orszag


