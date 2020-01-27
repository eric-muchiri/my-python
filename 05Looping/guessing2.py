import random

random_number = random.randint(1, 10)
guess = None

while guess != random_number:
    guess = input("pick a number between 1 and 10: ")
    guess = int(guess)
    if guess < random_number:
        print("Too low")
    elif guess > random_number:
        print("Too high")
    else:
        print("You won")
        play_again = input("Do you want to play again? (y/n)")
        if play_again == "y":
            random_number = random.randint(1, 10)
            guess = None
        else:
            print("Thank you for playing")
            break