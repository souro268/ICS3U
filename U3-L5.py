import math as m
def addFLO(a, b):
    check1 = False
    check2 = False
    try:
        a = float(a)
        check1 = True
    except:
        print("Bad data")
    try:
        b = float(b)
        check2 = True
    except:
        print("Bad data")
    if (check1 == True and check2 == True):
        return a+b
    if not (check1 == True and check2 == True):
        return "bad data"
    
    
def addINT(a, b):
    check1 = False
    check2 = False
    try:
        a = int(a)
        check1 = True
    except:
        print("Bad data")
    try:
        b = int(b)
        check2 = True
    except:
        print("Bad data")
    if (check1 == True and check2 == True):
        return a+b
    if not (check1 == True and check2 == True):
        return "bad data"

def myPOW(a,b):
    check1 = False
    check2 = False
    try:
        a = int(a)
        check1 = True
    except:
        print("Bad data")
    try:
        b = int(b)
        check2 = True
    except:
        print("Bad data")
    if (check1 == True and check2 == True):
        return m.pow(a,b)
    if not (check1 == True and check2 == True):
        return "bad data"

choice = input("Type 1 for Decimal numbers \n 2 for intergers\n 3 for power: ")

if (choice == '1'):
    a = input("Enter the first value: ")
    b = input("Enter the second value: ")
    print(addFLO(a,b))
elif (choice == '2'):
    a = input("Enter the first value: ")
    b = input("Enter the second value: ")
    print(addINT(a,b))
elif (choice == '3'):
    a = input("Enter the first value: ")
    b = input("Enter the second value: ")
    print(myPOW(a,b))
else:
    print("Please enter 1 or 2 or 3")
