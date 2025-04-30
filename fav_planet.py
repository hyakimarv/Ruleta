import random
import time

PLANETS = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

def fav_planet():
    while len(PLANETS) > 1:
        firstRandomPlanet = random.choice(PLANETS)
        secondRandomPlanet = random.choice(PLANETS)
        while firstRandomPlanet == secondRandomPlanet:
            secondRandomPlanet = random.choice(PLANETS)
        user_planet_pick = input(f"Do u like more {firstRandomPlanet} or {secondRandomPlanet}? ")
        if user_planet_pick == firstRandomPlanet:
            PLANETS.remove(secondRandomPlanet)
        elif user_planet_pick == secondRandomPlanet:
            PLANETS.remove(firstRandomPlanet)
        else:
            print("Invalid input, chose one of the following")
            continue
    print(f"Your favorite planet is {''.join(PLANETS)}")
    time.sleep(2)