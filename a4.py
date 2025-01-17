# Sourish Keshari 904147
# ICS 3U

def Date(Exp_Mo, Exp_Yr):
    Exp_Yr = str(Exp_Yr)
    Exp_Mo = int(Exp_Mo)
    month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for x in month:
        if Exp_Mo < 10:     
            if Exp_Mo == x:
                Exp_Mo = str(Exp_Mo)
                Exp_Mo = '0' + Exp_Mo
                return Exp_Yr + Exp_Mo
        if Exp_Mo >= 10:
            Exp_Mo = str(Exp_Mo)
            return Exp_Yr + Exp_Mo

def Comparison(DateArr, FirstNameArr, LastNameArr, CCtypeArr, CCNumber):
    for x in range(len(DateArr)):
        Total_Name = FirstNameArr[x] + ' ' + LastNameArr[x] + ':'
        variable = "%-35s\t%-13s %s %s" % (Total_Name, CCtypeArr[x], '#' + CCNumber[x], DateArr[x])
        if DateArr[x] < 202501:
            Status = ' EXPIRED'
            FileWrite.write(variable + Status + '\n')
        if DateArr[x] == 202501:
            Status = ' RENEW IMMEDIATELY'
            FileWrite.write(variable + Status + '\n')
        if DateArr[x] > 202501:
            Status = ' NOT EXPIRED'
            FileWrite.write(variable + Status + '\n')
    print(f"You sorting is done! Please open the file called '{FileNameWriting}' on you computer to view the output! :D")
    

def merge(arr, arr2, arr3, arr4, arr5, left, mid, right):
    # Merges two sorted subarrays into a single sorted array.
    for x in range(len(arr)):
        arr[x] = int(arr[x])
    n1 = mid - left + 1
    n2 = right - mid
    L, L2, L3, L4, L5 = [0] * n1, [0] * n1, [0] * n1, [0] * n1, [0] * n1
    R, R2, R3, R4, R5 = [0] * n2, [0] * n2, [0] * n2, [0] * n2, [0] * n2
    
    
    for i in range(n1):
        L[i] = arr[left + i]
        L2[i] = arr2[left + i]
        L3[i] = arr3[left + i]
        L4[i] = arr4[left + i]
        L5[i] = arr5[left + i]       
        
        
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
        R2[j] = arr2[mid + 1 + j]
        R3[j] = arr3[mid + 1 + j]
        R4[j] = arr4[mid + 1 + j]
        R5[j] = arr5[mid + 1 + j]
    
    i = j = 0
    k = left
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k], arr2[k], arr3[k], arr4[k], arr5[k] = L[i], L2[i], L3[i], L4[i], L5[i]

            i += 1
        else:
            arr[k], arr2[k], arr3[k], arr4[k], arr5[k] = R[j], R2[j], R3[j], R4[j], R5[j]
            j += 1
        k += 1
    
    while i < n1:
        arr[k], arr2[k], arr3[k], arr4[k], arr5[k] = L[i], L2[i], L3[i], L4[i], L5[i]
        i += 1
        k += 1
    
    while j < n2:
        arr[k], arr2[k], arr3[k], arr4[k], arr5[k] = R[j], R2[j], R3[j], R4[j], R5[j]
        j += 1
        k += 1



def merge_sort(arr, arr2, arr3, arr4, arr5, left, right):
    # Recursively sorts the array using the merge sort algorithm.
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, arr2, arr3, arr4, arr5, left, mid)
        merge_sort(arr, arr2, arr3, arr4, arr5, mid+1, right)
        merge(arr, arr2, arr3, arr4, arr5, left, mid, right)
        
        
       

    
filename = 'data.dat'  # The name of the file containing Wordle data
fh = open(filename, "r")  # Opens the file for

FileNameWriting = 'Soted_data.txt'
FileWrite = open(FileNameWriting, 'w')

FirstNameArr = []
LastNameArr = []
CCtypeArr = []
CCNumber = []
DateArr = []
n = 1




Temp_File_Line = fh.readline() # reads GivenName,Surname,CCType,CCNumber,Exp-Mo,Exp-Yr 
while n == 1:  # Loops through each line in the file
    try:
        tempvar = fh.readline()  # Reads one line from the file
    except:
        print("There is an error with reading the file. Please try again. ")
        n = 0
    tempvar.strip()  # Removes any leading/trailing whitespace
    try:
        First_Name, Last_Name, CC_Type, CC_Number, Exp_Mo, Exp_Yr = tempvar.split(',')
        FirstNameArr.append(First_Name.strip())
        LastNameArr.append(Last_Name.strip())
        CCtypeArr.append(CC_Type.strip())
        CCNumber.append(CC_Number.strip())
        temp = Date(Exp_Mo, Exp_Yr.strip())
        DateArr.append(temp)
        
    except ValueError:
        n = 0
    except Exception as err:  # Handles any other unexpected errors
        print(f"There has been an error. Error message: {err=}. Error type: {type(err)=}")
        n = 0
merge_sort(DateArr, FirstNameArr, LastNameArr, CCtypeArr, CCNumber,  0, len(DateArr) - 1)
Comparison(DateArr, FirstNameArr, LastNameArr, CCtypeArr, CCNumber)         
        
fh.close()
FileWrite.close()
