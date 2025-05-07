import time

def italianTest():
    print("Welcome to the Italian test! Are you ready to find out what percentage of you is Italian?")
    print()

    italianPercentage = 100

    pizzaAnanas = input("Can you put pineapple on pizza? (y/n): ")
    if pizzaAnanas.lower() == "y":
        print("Idiot?")
        italianPercentage -= 25
    else:
        print("Good job!")

    greeting = input("How do you say hello to friends in Italian? ")
    if greeting.lower() == "ciao" or greeting.lower() == "salve":
        print("Bene!!")
    else:
        print("Bro nah")
        italianPercentage -= 25

    pizza = input("Margherita or Hawaii? ")
    if pizza.lower() == "hawaii":
        print("Didn't you understand that you can't put pineapple on pizza?...")
        italianPercentage -= 25
    else:
        print("Bravo! Bravissimo!! Bravissimi!!!")

    italianName = input("Anna or Sasha? ")
    if italianName.lower() == "anna":
        print("Perfetto!!!!!")
    else:
        print("Omg..")
        italianPercentage -= 25

    print(f"You are Italian on {italianPercentage}%")
    time.sleep(2)