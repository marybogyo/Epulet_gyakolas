import random
erme_lista = []
def penzerme():
    i = 0
    szoveg = ""
    while i < 7:
        vel = int(random.random() * 2) + 1
        erme_lista.append(vel)

        if erme_lista[i] == 1:
            szoveg += "FEJ"
        else:
            szoveg += "ÍRÁS"

        if i != 6:
            szoveg += "-"

        i += 1
    print(f"II/A, B, C:\n\t {szoveg}")


def fejek_szama():
    i = 0
    fej_szam = 0
    while i < len(erme_lista):
        if erme_lista[i] == 1:
            fej_szam += 1
        i += 1
    return fej_szam


def konzol_kiir():
    print(f"II/D, E:\n\t A fejek száma: {fejek_szama()}")


def file_kiir():
    fajl = open("fejek.txt", "w", encoding="utf-8")
    fajl.write(f"II/F\n\t A fejek száma: {fejek_szama()}")
    fajl.close()