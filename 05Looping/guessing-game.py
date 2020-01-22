import random
#get a eandom number between one and 10 inclusive
random_number = random.randint(1, 10)
#print(random_number)
guess = input("pick a number between 1 and 10: ")
guess = int(guess)
if guess == random_number:
    print("you got it")
elif guess > random_number:
    print("Too high")
else:
    print("Too low")