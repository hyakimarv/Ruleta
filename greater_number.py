import time
import random

def greaterNumber():

    first_random_number = random.randint(1, 1000)
    second_random_number = random.randint(1, 1000)

    print(first_random_number, second_random_number)

    user_input = input("What number is greater (1 or 2 or 3 IF THEY ARE EQUAL): ")

    if first_random_number > second_random_number and user_input == "1":
        print(f"Correct! {first_random_number} > {second_random_number}")
    elif first_random_number < second_random_number and user_input == "2":
        print(f"Correct! {first_random_number} < {second_random_number}")
    elif first_random_number > second_random_number and user_input == "2":
        print(f"Incorrect( {first_random_number} > {second_random_number})")
    elif first_random_number < second_random_number and user_input == "1":
        print(f"Incorrect( {first_random_number} < {second_random_number})")
    elif first_random_number == second_random_number and user_input == "1":
        print(f"Incorrect( {first_random_number} = {second_random_number})")
    elif first_random_number == second_random_number and user_input == "2":
        print(f"Incorrect( {first_random_number} = {second_random_number})")
    elif first_random_number == second_random_number and user_input == "3":
        print(f"Correct! {first_random_number} = {second_random_number}")
    else:
        print("You wrote incorrect number, read the rules and play again")
        time.sleep(2)
        greaterNumber()
    time.sleep(2)


