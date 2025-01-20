n = 0
arr = []
v = ['a', 'e', 'i', 'o', 'u', 'y']
while n == 0:
    temp = input()
    if temp == 'quit!':
        n = 1
    else:
        arr.append(temp)
        
for x in range(len(arr)):
    try:
        if len(arr[x]) > 4:
            temp = arr[x]
            for y in range(len(temp)):
                if temp[y] == 'o' and temp[y+1] == 'r':
                    for i in range(len(v)):
                        if not temp[y-1] == v[i]:
                            temp[y] = 'ou'
                            arr[x] = temp
                            
                            
        else:
            pass
    except:
        pass

print(arr)
        

for x in range(len(arr)):
    print(arr[x])
    
        
