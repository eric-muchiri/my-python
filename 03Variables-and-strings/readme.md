# Variables and strings

Variable - Container that holds data  
Example x in the case below  
variable name on the left and a corresponding value  

```python
x = 100  
print(x)  
```

Variable data can change  

```python
x = 100 + 32
print(x)
```

## naming restrictions

* Variables start with a letter/underscore  
* The rest of the name consist of numbers, letters, underscores  
* Names are case sensitive  

## Convections

* Snake case (underscores between words)  
* Variables be in lower case (with exceptions)  
* Capital snake case for constants  
* upperCamelCase for classes  
* Variables that start and end in two underscores  are called dunder and are private  or be left alone

## Data Types

Bool - True or False values. Has to begin in caps  
Int - An integer (1,3,8)  
str - String (sequence of unicode characters) e.g "me"  
list - An ordered sequence of values of other data types ['1', '2'], ['a', 'b']  
dict - a collection of key:value pairs e.g{"name": "Eric"}  

## Dynamic Typing

Python is flexible about re-assigning variables to different types  
Example

```python
#bool
my_var = True
#string
my_var = "Eric"
#int
my_var = 4
```

### concatenation

Joining strings  
We use the + sign  

```python
name = "Eric"
hobby = "drawing"

print(name + " likes "+ hobby)
```

__Interpolating variables__  
You cannot concatenate other data types  
What if you need to concatenate a number?  
We use __`f`__ at the beginning and the variable name in braces  

```python
x=7
statement = f"there are {x} days in a week"
print(statement)
```

## String indexes  

The position of characters  
In python, they begin from 0 (zero)  

```python
# String indexes
name = "Eric"
print(name[0])
# -ve counts from the end e.g the last character is
print(name[-1])
```
