name = input("Enter your name: ")
if name == "Doe":
    print("you own the repo")
elif name == "John":
    print("you are a contributor")
else:
    print("anonymous")

# multiple Elifs
myage = input("Enter your age in numbers: ")
age = int(myage)
if age < 18:
    print("You are still a child")
elif 18 <= age <=24:
    print("Young adult")
elif 25 <= age <=35:
    print("cool")
else:
    print("somewhat older")