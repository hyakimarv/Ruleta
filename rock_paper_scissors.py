import random
import time

BOT_CHOICE = ["Rock", "Paper", "Scissors"]
def playRPS():

    player_choice = input("Enter your choice (Rock, Paper or Scissors): ")
    bot_choice = random.choice(BOT_CHOICE)

    if player_choice == bot_choice:
        print(f"Bot picked {bot_choice}")
        print("It's a tie!")

    elif player_choice == "Rock" and bot_choice == "Scissors":
        print(f"Bot picked {bot_choice}")
        print("You won!")

    elif player_choice == "Rock" and bot_choice == "Paper":
        print(f"Bot picked {bot_choice}")
        print("You lost!")

    elif player_choice == "Paper" and bot_choice == "Rock":
        print(f"Bot picked {bot_choice}")
        print("You won!")

    elif player_choice == "Paper" and bot_choice == "Scissors":
        print(f"Bot picked {bot_choice}")
        print("You lost!")

    elif player_choice == "Scissors" and bot_choice == "Rock":
        print(f"Bot picked {bot_choice}")
        print("You lost!")

    elif player_choice == "Scissors" and bot_choice == "Paper":
        print(f"Bot picked {bot_choice}")
        print("You won!")

    else:
        print("Only Rock, Paper and Scissors are allowed.")
        playRPS()
    time.sleep(2)
