import random

while True:
    level = input("Level: ")
    while not level.isdigit() or int(level) < 1:
        level = input("Level: ")

    random_number = random.randrange(int(level))
    guess = None

    guess = input("Guess: ")
    while not guess.isdigit() or int(guess) < 0:
        guess = input("Guess: ")
    guess = int(guess)

    if guess < random_number:
        print("Too small!")
    elif guess > random_number:
        print("Too large!")
    else:
        print("Just right!")
        break
