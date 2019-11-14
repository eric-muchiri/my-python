#bool
my_var = True
#string
my_var = "Eric"
#int
my_var = 4

print(my_var)

#string concatenation
name = "Eric"
hobby = "drawing"

print(name + " likes "+ hobby)

# Interpolating variables
x=7
statement = f"there are {x} days in a week"
print(statement)

# String indexes
name = "Eric"
print(name[0])
# -ve counts from the end e.g the last character is
print(name[-1])

#Converting Data types
myDecimal = 13.4578
newInt = int(myDecimal)
#chops off the decimal
print(newInt)

list1 = [1,2,3,5]
list1_as_string = str(list1)
print(list1_as_string)

#simple milage converter
print("How many kilometers did you run today")
kms = input()
miles = float(kms)/1.60934
print(f"the distance in miles is {miles}")