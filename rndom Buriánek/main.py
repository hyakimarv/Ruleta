import random
jidla = ["pizza", "špagety", "hamburger", "sushi", "řízek"]
v8 = random.choice(jidla)
index = jidla.index(v8)
print("Vybral jsem jídlo " + v8 + " co se vybralo na indexu " + str(index) + " v poli")