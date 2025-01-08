def Date(Exp_Mo, Exp_Yr):
    Exp_Yr = str(Exp_Yr)
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
    
def mergeData(month, date, year):
    # Converts month, day, and year into a single YYYYMMDD string.
    month = month.lower()
    month_arr = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    try:
        for i in range(len(month_arr)):
            if month == month_arr[i]:
                month = str(i + 1)
        if int(month) < 10:
            # Padding single-digit months with a leading zero
            month = '0' + month
        return year + month + date
    except:
        print("Please enter a valid month and try again.")
        User_Inputs(num_arr, word_arr, mergeData, merge_sort, binary_search, 0)



def merge(arr, arr2, arr3, arr4, arr5, left, right):
    # Merges two sorted subarrays into a single sorted array.
    n1 = mid - left + 1
    n2 = right - mid
    L, L2, L3, L4, L5 = [0] * n1, [0] * n1, [0] * n1, [0] * n1, [0] * n1  # Temporary arrays for left subarray
    R, R2, R3, R4, R5 = [0] * n2, [0] * n2, [0] * n2, [0] * n2, [0] * n2  # Temporary arrays for right subarray
    
    
    for i in range(n1):
        L[i] = arr[left + i]
        L2[i] = arr2[left + i]
        L3[i] = arr3[left + i]
        L4[i] = arr4[left + i]
        L5[i] = arr5[left + i]       
        
        
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
        R2[j] = arr2[mid + 1 + j]
    
    i = j = 0
    k = left
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k], arr2[k] = L[i], L2[i]
            i += 1
        else:
            arr[k], arr2[k] = R[j], R2[j]
            j += 1
        k += 1
    
    while i < n1:
        arr[k], arr2[k] = L[i], L2[i]
        i += 1
        k += 1
    
    while j < n2:
        arr[k], arr2[k] = R[j], R2[j]
        j += 1
        k += 1



def merge_sort(arr, arr2, arr3, arr4, arr5, left, right):
    # Recursively sorts the array using the merge sort algorithm.
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, arr2, arr3, arr4, arr5, left, right)
        merge_sort(arr, arr2, arr3, arr4, arr5, left, right)
        merge(arr, arr2, arr3, arr4, arr5, left, right)
    #  
    
filename = 'data.dat'  # The name of the file containing Wordle data
fh = open(filename, "r")  # Opens the file for

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
        FirstNameArr.append(First_Name)
        LastNameArr.append(Last_Name)
        CCtypeArr.append(CC_Type)
        CCNumber.append(CC_Number)
        DateArr.append(Date(Exp_Mo, Exp_Yr))       
        
        
    except ValueError:
        n = 0
    except Exception as err:  # Handles any other unexpected errors
        print(f"There has been an error. Error message: {err=}. Error type: {type(err)=}")
        n = 0
merge_sort(DateArr, FirstNameArr, LastNameArr, CCtypeArr, CCNumber,  0, len(DateArr) - 1)

        
        
    

