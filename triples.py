import math as m


inputs = int(input(""))
lists = []
for n in range(3,inputs):
    a = m.pow(n,2)
    b = m.pow((m.floor(n/2)) * (n+1),    2)
    c = m.pow((m.floor(n/2)) * (n+1) + 1,2)
    total = a+b
    if total == c:
        lists.append(n)
        print(f"A = {m.sqrt(a)} \n B = {m.sqrt(b)} \n  C = {m.sqrt(c)} \n toatl = {m.sqrt(total)}")
        print("-----------------------------------------")
print(lists)
