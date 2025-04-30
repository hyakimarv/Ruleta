import random
import time

def mathGame():
    firstNumber = random.randint(1, 1000)
    secondNumber = random.randint(1, 1000)
    print(f"{firstNumber} + {secondNumber} = ?")
    while True:
        userAnswer = int(input())
        if userAnswer == firstNumber + secondNumber:
            print(f"Yes, {firstNumber} + {secondNumber} = {userAnswer}")
            break
        else:
            print("No, its not, try again!")
    time.sleep(2)