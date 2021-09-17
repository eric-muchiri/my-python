#filter even numbers
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = list(filter(lambda x : x % 2==0, l))

print(evens)