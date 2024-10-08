import math as m
def factorize(x):
    lists= []
    i = m.floor(m.sqrt(x))
    for j in range(1,i+1):
        if x%j == 0 and x%j != x:
            lists.append(j)
        if x//j != j and x//j !=x:
            lists.append(x//j)
    lists.sort()
    return lists
def check(lists, x):
    sum = 1
    for k in range(len(lists)):
        sum += lists[k]
    if sum > x:
        print(f"{sum} is deficient")
    elif sum < x:
        print(f"{sum} is perfect")
    elif sum < 0:
        print("GoodBye!")
    return sum
    
        
x = float(input("Enter the number you want to factoize: "))
fac = factorize(x)
checks = (fac, x)
print(fac)
print(check)


    
        
