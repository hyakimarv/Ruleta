import random
import time

SINGERS = ["MACAN", "Rammstein", "Nemo", "Morgenshtern", "Karel Gott", "Maneskin", "Monatik", "Ed Sheeran", "Travis Scott"]

def favSinger():
    while len(SINGERS) > 1:
        firstRandomSinger = random.choice(SINGERS)
        secondRandomSinger = random.choice(SINGERS)
        while firstRandomSinger == secondRandomSinger:
            secondRandomSinger = random.choice(SINGERS)
        user_singer_pick = input(f"Do u like more {firstRandomSinger} or {secondRandomSinger}? ")
        if user_singer_pick == firstRandomSinger:
            SINGERS.remove(secondRandomSinger)
        elif user_singer_pick == secondRandomSinger:
            SINGERS.remove(firstRandomSinger)
        else:
            print("Invalid input, chose one of the following")
            continue
    print(f"Your favorite singer is {''.join(SINGERS)}")
    time.sleep(2)