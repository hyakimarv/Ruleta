import random
import time

def memoryGame():
    memoryNumber = random.sample(range(1, 10), 4)
    print(" ".join(str(num) for num in memoryNumber))
    time.sleep(0.5)
    print("\n" * 100)
    user_input = input("What were the numbers? ")
    userMemoryNumber = [int(char) for char in user_input]

    if userMemoryNumber == memoryNumber:
        print("Congrats! It's the correct sequence!")
    else:
        print("Almost there! The correct numbers were:", memoryNumber)
    time.sleep(2)