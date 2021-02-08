# GMIT PforCS
# Author Michal Sudol G00398852@gmit.ie
# Python - The Collatz Sequence

print ("Hi, to hit Enter to Proceed..")

def collatz(num):
    while num > 1:
        if num % 2 == 0:
            print(num//2)
            num = num //2
        elif num % 2 ==1:
            print(3*num+1)
            num = 3*num+1
        else:
            print(num)

def getNum():
    global num
    num = (input("> "))
    try:
        num = int(num)
    except ValueError:
        print('Hi again, Plese enter any number and hit Enter again..')
        getNum()
getNum()
collatz(num)