import random
import time

COUNTRIES = [
    "Italy", "America", "Czechia", "France", "Spain",
    "Great Britain", "Ukraine", "Russia", "Deutschland",
    "Weißrussland", "Brazil"
]

def favCountry():
    countries_copy = COUNTRIES.copy()
    while len(countries_copy) > 1:
        firstRandom = random.choice(countries_copy)
        secondRandom = random.choice(countries_copy)
        while firstRandom == secondRandom:
            secondRandom = random.choice(countries_copy)
        user_pick = input(f"Do u like more {firstRandom} or {secondRandom}? ")
        if user_pick == firstRandom:
            countries_copy.remove(secondRandom)
        elif user_pick == secondRandom:
            countries_copy.remove(firstRandom)
        else:
            print("Invalid input, chose one of the following")
            continue
    print(f"Your favorite country is {''.join(countries_copy)}")
    time.sleep(2)
