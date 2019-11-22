#ask for age
age = input("How old are you: ")
#cast into an int
age = int(age)
#check if input is empty
if age:
    #18-21 wristband
    if age >=18 and age < 21:
        print("You need a wristband")
    #21+ can drink
    elif age >= 21:
        print("you can drink")
    #too young
    else:
        print("sorry you are too young")
else:
    print("Please enter an age")
