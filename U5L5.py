def f(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        temp = f(n-1) + f(n-2)
        return temp
        

print('Program for printing the Fibonacci sequence!')
inputs = int(input("Please input a whole number: "))
for i in range(inputs+ 1):
    print(f(i), end = ' ')
