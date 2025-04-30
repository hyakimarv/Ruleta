import time
from getpass import getuser
import time
from games import fav_country, fav_planet, fav_sibling, guess_number, guess_the_word, is_palindrome, italian_test, \
    math_game, memory_number, rock_paper_scissors, text_game, fav_singer, greater_number, english_spanish

username = getuser()

print(f"Welcome to Infissino Minigamissino, {username}!")
time.sleep(2)

def startMenu():
    print("""Minigames:
          1. Favorite Country
          2. Favorite Planet
          3. Favorite Singer
          4. Favorite Sibling
          5. Guess the number
          6. Guess the word
          7. Is palindrome
          8. Italian test
          9. Math Game
          10. Memory number
          11. Rock, paper, scissors
          12. Text Game
          13. Greater number
          14. English or Spanish 
          15. Exit""")

def start_game(choice):
    if choice == 1:
        fav_country.favCountry()
    elif choice == 2:
        fav_planet.fav_planet()
    elif choice == 3:
        fav_singer.favSinger()
    elif choice == 4:
        fav_sibling.siblingsGame()
    elif choice == 5:
        guess_number.guessNumberGame()
    elif choice == 6:
        guess_the_word.guessWord()
    elif choice == 7:
        is_palindrome.palindromeGame()
    elif choice == 8:
        italian_test.italianTest()
    elif choice == 9:
        math_game.mathGame()
    elif choice == 10:
        memory_number.memoryGame()
    elif choice == 11:
        rock_paper_scissors.playRPS()
    elif choice == 12:
        text_game.textGame()
    elif choice == 13:
        greater_number.greaterNumber()
    elif choice == 14:
        english_spanish.englishSpanish()
    elif choice == 15:
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice! Exiting...")
        exit()

if __name__ == "__main__":
    while True:
        startMenu()
        try:
            choice = int(input("Please choose a game by number: "))
            start_game(choice)
        except ValueError:
            print("Please enter a valid number.")