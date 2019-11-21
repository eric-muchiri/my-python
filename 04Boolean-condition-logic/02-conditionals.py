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

# truthiness
x = 1
x is 1
# is is an equivalent to double equals
# Things have truthiness and falsiness
# naturally false things: empty objects, empty strings, none
if 1:
    print('awesome!!')
#We can check for empty strings using truthiness e.g if user doesn't input anything

# comparisons
# returns true or false
print (4>5)
print (8<10)
print(6==6)
print(3>=4)
print(-9<=9)