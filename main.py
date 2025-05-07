import random

predmety = ["matematika", "čeština", "dějepis", "výtvarná", "tělocvik"]
            
v10 = random.choice(predmety)


index = predmety.index(v10)

print("Vybral jsem předmět " + v10 + " co se vybral na indexu " + str(index) + " v poli")