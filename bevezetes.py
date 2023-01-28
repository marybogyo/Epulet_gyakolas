def varazslo():
    jatekos_nev = input("I/A: \n\t Játékos neve: ")
    szerep = input("\t szerepkör: ")
    if szerep == "varázsló":
        print(f"I/B\n\t Üdvözlünk {jatekos_nev}, 2 életed van!")
    elif szerep == "harcos":
        print(f"I/B\n\t Üdvözlünk {jatekos_nev}, 10 életed van!")
    else:
        print(f"I/B\n\t Üdvözlünk {jatekos_nev}, 8 életed van!")
