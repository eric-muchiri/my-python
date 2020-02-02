tasks = ["setup","learn", "code", "relax"]
print (len(tasks))
r = range (1, 10)
print(list (r))
numbers = list (range(1,10))
print (numbers)

print(tasks[1])
#using a negative index to print the last item
print(tasks[-1])

# check if an item is in a list
# We use the in keyword
#returns true or false
print("learn" in tasks)
#Iterate through a list
for number in numbers:
    print(number)

