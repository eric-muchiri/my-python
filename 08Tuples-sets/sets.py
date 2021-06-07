#do not have duplicate values
#elements are not oredered
s={1,3,4,5}

#accessing
print(4 in s)# returns either true or false

for number in s:
    print(number)

#set methods
#add
s.add(6)

print(s)

#remove
s.remove(4)
print(s)

#set math
#union | combine sets with no duplicates

s1={1,2,3}
s2={2,3,4,5}

print(s1 | s2)

#intersection &
#print elements that appear in both sets

print(s1 & s2)

#comprehension
sq={x**2 for x in range(10)}
print(sq)