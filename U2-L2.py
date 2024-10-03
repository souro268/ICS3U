import math

x = input("Please input a whole number (1-20): ")
x = int(x)
y = input("Please input another nonzero whole number(1-20): ")
y = int(y)
print("Now deciding if", y, "is a factor of", x, "...")
rem = x % y
if (rem == 0) and (y != 0) and (x < 20) and (x > 1) and (y < 20) and (y > 1):
    print("Yes!", y, "is a factor of", x)
else:
    print("Re-enter your numbers. 0 is not allowed for the second number")
    print("and x and y have to be 1- 20")
