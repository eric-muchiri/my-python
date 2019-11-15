# Boolean and condition logic

## Boolean  

 :sparkles: True or false values  

## Getting user input

A built in function to get the input fron the console  
The result can be stored in a variable.  
Example:

```python
name = input("Enter your name: ")
print("You are "+ name)
```

## Conditionals

Represents different paths a program can take based on some comparison  
**If statements**  
if condition1:  
    action to take  
elif codition2:  
    alternative action  
else:
    default  
`elif` is an equivalent to `else if` in other languages  

```python
name = input("Enter your name: ")
if name == "Doe":
    print("you own the repo")
elif name == "John":
    print("you are a contributor")
else:
    print("anonymous")
```