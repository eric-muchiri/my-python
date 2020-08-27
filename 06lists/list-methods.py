numberList = [1, 2, 3, 4, ]
# adding items to a list
numberList.append(5)
#this doesnot work
#numberList.append(6,7,8,9)
numberList.append([6,7,8,9])
#result
#[1, 2, 3, 4, 5, [6, 7, 8, 9]]


print(numberList)