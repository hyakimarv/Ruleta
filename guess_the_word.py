import random
import time

WORDS = ["Apple", "Samsung", "BMW", "Mercedes", "Banana", "Pasta", "Anna", "Milano"]

def guessWord():
    random_word = random.choice(WORDS)
    attempts = 0
    print("Try to guess the word!")
    while True:
        hint = random_word[:attempts + 1]
        print(f"Hint: {hint}")
        user_guess = input("Guess the word: ")
        attempts += 1
        if user_guess == random_word:
            print(f"Congrats! You guessed the word! It was {random_word}")
            break
        elif attempts == len(random_word) - 1:
            print(f"Sorry, you lost! The word was {random_word}")
            break
    time.sleep(2)
