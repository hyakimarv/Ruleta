import random
import time

def guessNumberGame():
    randomNumber = random.randint(1, 100)
    print("Guess a number between 1 and 100")
    while True:
        userNumber = int(input("Enter yr number: "))
        if userNumber > randomNumber:
            print("Your guess is too high")
        elif userNumber < randomNumber:
            print("Your guess is too low")
        else:
            print(f"You won! I guessed {randomNumber}")
            break
    time.sleep(2)