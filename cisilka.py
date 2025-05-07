import random

cisla = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nahodne_cislo = random.choice(cisla)

index_cisla = cisla.index(nahodne_cislo)

print("Vybral jsem číslo " + str(nahodne_cislo) + " na indexu " + str(index_cisla))
