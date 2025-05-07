import random
pole = ["pes", "kočka", "chobotnice", "žralok", "žába"]
vybrane_zvire = random.choice(pole)
index_vybrane_zvire = pole.index(vybrane_zvire)
print(f"Vybral jsem zvíře {vybrane_zvire} co se vybralo na indexu {index_vybrane_zvire}")


