import time

def textGame():
    print("Welcome to the Fun Text Game!")

    food = input("What is your favorite food? ")
    name = input("What is your favorite name? ")
    teacher = input("Who is your favorite teacher? ")

    story = f"""
    Once upon a time, {name} went to a restaurant and ordered their favorite food, {food}.
    But as soon as they took a bite, they realized that their favorite teacher, {teacher}, was sitting at the next table!
    They couldn't stop laughing because {teacher} had the same dish, but they were using a fork in the most unusual way.
    {name} thought, "This is the best meal I've ever had — and the funniest teacher I've ever met!"
    """

    print("\nHere is your story:\n")
    print(story)
    time.sleep(2)
