def add(arr2):
    temp = ''
    for x in range(len(arr2)):
        temp = temp + arr2[x]
    return temp

n = 0
arr = []
arr2 = []
v = ['a', 'e', 'i', 'o', 'u', 'y']
while n == 0:
    temp = input()
    if temp == 'quit!':
        n = 1
    else:
        arr.append(temp)
        
        
for x in range(len(arr)):

    if len(arr[x]) > 4:
        temp = arr[x]
        for i in range(len(temp)):
            arr2.append(temp[i])
        for y in range(len(temp)):
            if arr2[y] == 'o' and arr2[y+1] == 'r':
                for i in range(len(v)):
                    if not arr2[y-1] == v[i]:
                        arr.pop
                        arr.pop
                        arr2.append('our')
                        arr[x] = add(arr2)
                        
                        
    else:
        pass


print(arr)
        
