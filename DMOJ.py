
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
        for i in range(len(arr[x])):
            if temp[i] == 'o' and temp[i+1] == 'r':
                if not temp[i-1] in v:
                    temp2 = temp[:(i+1)]
                    temp = temp2 + 'ur' + temp[i+2:]
                    arr[x] = temp
            if temp[i] == 'o' and temp[i+1] == 'u' and temp[i+2] == 'r':
                 pass
            else:
                pass
    else:
        pass
for x in arr:
    print(x)
