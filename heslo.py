import random

města = ["Praha","Brno","Ostrava","Plzeň","Olomouc"]
v12 = random.choice(města)
index = města.index(v12)

print(f"Vybral jsem město {v12} co se vybralo na indexu {index} v poli")