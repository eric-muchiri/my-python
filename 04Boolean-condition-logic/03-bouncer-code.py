#ask for age
age = input("How old are you: ")
#18-21 wristband
if int(age) >=18 and int(age) < 21:
    print("You need a wristband")
#21+ can drink
elif int(age) >= 21:
    print("you can drink")
#too young
else:
    print("sorry you are too young")
