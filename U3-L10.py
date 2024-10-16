import math as m
inputs = int(input(""))
lists = []
for n in range(3,inputs + 1, 1):
    
    if(n%2 == 1):
        a = m.pow(n,2)
        b = m.pow((m.floor(n/2)) * (n+1),    2)
        c = m.pow((m.floor(n/2)) * (n+1) + 1,2)
        total = a+b
        if total == c:
            lists.append(n)
            print(f"A = {m.sqrt(a)} \nB = {m.sqrt(b)} \nC = {m.sqrt(c)} \ntotal = {m.sqrt(total)}")
            print("----------------------------------------------")
    elif(n%2 == 0):
        z = m.pow(n,2)/4
        a1 = m.pow(n,2)
        b1 = m.pow(z - 1, 2)
        c1 = m.pow(z + 1, 2)
        total1 = a1+b1
        if total1 == c1:
            lists.append(n)
            print(f"A = {m.sqrt(a1)} \nB = {m.sqrt(b1)} \nC = {m.sqrt(c1)} \ntotal = {m.sqrt(total1)}")
            print("----------------------------------------------")
print(lists)
        
