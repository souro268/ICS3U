'''
16 3 2 13
5 10 11 8
9 6 7 12
4 15 14 1
'''

def Vertical():
    
    x = 0
    temp1 = arr[x] + arr2[x] + arr3[x] + arr4[x]
    temp2 = arr[x+1] + arr2[x+1] + arr3[x+1] + arr4[x+1]
    temp3 = arr[x+2] + arr2[x+2] + arr3[x+2] + arr4[x+2]
    temp4 = arr[x+3] + arr2[x+3] + arr3[x+3] + arr4[x+3]
    
    if temp == temp2 and temp2 == temp3 and temp3 == temp4:
        return True
    else:
        return False
def Hor():
    temp1 = arr[0] + arr[1] + arr[2] + arr[3]
    temp2 = arr2[0] + arr2[1] + arr2[2] + arr2[3]
    temp3 = arr3[0] + arr3[1] + arr3[2] + arr3[3]
    temp4 = arr4[0] + arr4[1] + arr4[2] + arr4[3]
    if temp == temp2 and temp2 == temp3 and temp3 == temp4:
        return True
    else:
        return False
def Dia():
    temp1 = arr[0] + arr2[1] + arr3[2] + arr4[3]
    temp2 = arr[3] + arr2[2] + arr3[1] + arr4[0]
    if temp == temp2:
        return True
    else:
        return False
    
def check():
    if Vertical() == True and Hor() == True and Dia() == True:
        return 'magic'
    else:
        return 'not magic'
arr1 = []


for x in range(4):
    temp = input(" INPUT ")
    one, two, three, four = temp.split(' ')
    
    one = int(one)
    two = int(two)
    three = int(three)
    four = int(four)
    
    arr1.append(one)
    arr1.append(two)
    arr1.append(three)
    arr1.append(four)

arr = [arr1[0], arr1[1], arr1[2], arr1[3]]
arr2 = [arr1[4], arr1[5], arr1[6], arr1[7]]
arr3 = [arr1[8], arr1[9], arr1[10], arr1[11]]
arr4 = [arr1[12], arr1[13], arr1[14], arr1[15]]

print(check())

