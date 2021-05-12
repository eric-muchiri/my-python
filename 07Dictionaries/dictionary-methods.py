#dictionary methods
#clear
#clears all keys and values in a dictionary
d = dict(a=1, b=2, c=3)
print(d)
d.clear()
print(d)
#pop
#remove an item
#a key must be provided
John = {
    "gender": "male",
    "age": 32,
    "nationality": "kenyan",
    "isMarried": True
}
John.pop("age")
print(John)

#popitem
#removes a random key in a dictionary
#takes no arguments

John.popitem()

#update
mike = {
    "city": "Nairobi"
}

mike.update(John)
print(mike)