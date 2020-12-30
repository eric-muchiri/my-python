John = {
    "gender": "male",
    "age": 32,
    "nationality": "kenyan",
    "isMarried": True
}

print(John)

cat = dict(name = "kitty")

print(cat)

#accessing individual data
#pass in a key

print(John['gender'])

#iterating dictionaries
#.values for values
for value in John.values():
    print(value)

#.keys for keys
for key in John.keys():
    print(key)

#.items for all keys and values
for key,value in John.items():
    print(key,value)
#in a dict order is not guranteed unlike lists