
#count = int(input("Enter nunber: "))
count = 15

for i in range(1, count, 2):
    x = "*"
    b = " "
    x = x * (i * 2)
    b = b * count
  
    print(b*i, end = f"{x+(x*(x*i))}")
    count -= 2

count = 15
lock = count
for j in range(count, -1, -1):
    
    y = "*"
    a = " "
    a = a * (count - (lock - 1))
    y = y * (j * 2)
    count += 1
    print(f"{a} {y} {a}")




# count = int(input("Enter number: "))
# while ((count % 2) == 1):
#     count = int(input("Enter number: "))
count = 18
temp = 0
lock = count
for x in range(1, (count*2), 2):
    s = "#"
    i = "1"
    s = s * temp
    i = i * (count - (lock - 1))
    print(f"{i}{s}{i}")
  
    if temp < count2/2:
        temp += 1
        temp2 +=1
    else:
        temp2 -=1
    
    


     
    


