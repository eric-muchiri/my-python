print("how many times do I say hello?")
num = input()
num = int(num)

for time in range (num):
    print("Hello")
#loop2 unlucky
#tesnNum = input("Input your test number: ")
#tesnNum = int(tesnNum)
for number in range (21):
    if number == 4 or number == 13:
        print(number)
        print(" unlucky")
    if number%2 == 0 and number != 4:
        print(number)
        print(" even")
    if number%2 == 1 and number != 13:
        print(number)
        print(" odd")        
