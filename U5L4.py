filename = 'words40.dat'
fh = open(filename, 'r')

arr = [0]*40

for i in range(40):
    strtemp = ''
    strtemp = fh.readline()
    strtemp = strtemp.strip()
    arr[i] = strtemp
        
for j in range(0, len(arr)):
    for k in range(0, i):
        if arr[j] < arr[k]:
            arr[j], arr[k] = arr[k], arr[j]

for i in range(1, 5):
    for j in range(1,11):
        print(arr[i*j -1], end = " ")
    print('\n')
print('40 words.')

