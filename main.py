import bevezetes
import sorozat
import epuletek

bevezetes.varazslo()
epuletek.beolvas()

sorozat.penzerme()
sorozat.fejek_szama()
sorozat.konzol_kiir()
sorozat.file_kiir()
print(f"III/A, B:\n\t Az épületek száma:{epuletek.epluet_szam()}")
print(f"III/C:\n\t Az 555 lábnál magasabb épületek száma: {epuletek.magasabb_epulet()}.")

print(f"III/D\n\t A legöregebb épület országa: {epuletek.legoregebb_epulet()}")
