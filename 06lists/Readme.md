# lists

A collection of items  
A way of combining data into one variable  

## Creating lists

Consists of a name and items in square brackets  
Items are separated by commas  

```python
tasks = ["setup","learn", "code", "relax"]
```

Check the number of items in a list  

```python
len(list_name)
#e.g
len(tasks)
```

__The `list` function__
Another way to create a list  
Example using ranges:

```python
#r = range (1, 10)
#print(list (r))
numbers = list (range(1,10))
print (numbers)
```

## Accessing data in a list

Lists start counting from 0  
`listname[index]` gives the item in that position  

```python
print(tasks[1])
```

A negative number can be used to index backwards  

```python
print(tasks[-1])
```

The above prints the last item  

## Checking for Items in a list

The `in` keyword is used to check whether an itm is in a list  
Returns either true or false  

```python
print("learn" in tasks)
```

## list methods

__Append__  
Add items at the end of a list  
Suitable for adding a songle value

__Extend__  
Suitable for adding multiple items

## list comprehension

Different from looping - We can do it in a single line
