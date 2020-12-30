# Dictionaries

A data structure consisting of key-value pairs  
We use keys to describe the data and values to represent the data  
Example  

```py
John = {
    "gender": "male",
    "age": 32,
    "nationality": "kenyan",
    "isMarried": True
}

print(John)
```

We can also use the `dict` function  
You assign values to keys by passing values and keys separated by an `=`  

Example  

```py
cat = dict(name = "kitty")

print(cat)
```

## Accessing individual values

Passing a key gives the corresponding value  

```py
print(John['gender'])
```
