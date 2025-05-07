import random
import time

def siblingsGame():
    SIBLINGS = []
    quantity_siblings = int(input("Enter many siblings u would like to add (Ex. 5): "))
    for i in range(quantity_siblings):
        add_siblings = input("Who would u like to add (Ex. Mother): ")
        SIBLINGS.append(add_siblings)
    print(f"Fine! Your siblings are: {SIBLINGS}")
    time.sleep(2)
    while len(SIBLINGS) > 1:
        firstRandomSibling = random.choice(SIBLINGS)
        secondRandomSibling = random.choice(SIBLINGS)
        while firstRandomSibling == secondRandomSibling:
            secondRandomSibling = random.choice(SIBLINGS)
        user_sibling_pick = input(f"Do u like more {firstRandomSibling} or {secondRandomSibling}? ")
        if user_sibling_pick == firstRandomSibling:
            SIBLINGS.remove(secondRandomSibling)
        elif user_sibling_pick == secondRandomSibling:
            SIBLINGS.remove(firstRandomSibling)
        else:
            print("Invalid input, chose one of the following")
            continue
    print(f"Your favorite sibling is {''.join(SIBLINGS)}")
    time.sleep(2)