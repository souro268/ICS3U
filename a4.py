
'''
To-Do
- fix the num_arr and word_arr, they seem to be the same array. prob some indexing or swaping error
- fix seaching for word/date
- add num and word into dictionary 
- variable dictionary
- 


Oct 01 2023 BERET
Oct 02 2023 MERRY
Oct 03 2023 WHILE
Oct 04 2023 SPURT
Oct 05 2023 BUNCH
Oct 06 2023 CHIME
20231006-CHIME
'''
def mergeData(month, date, year):
    month = month.lower()
    montharr = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    year_arr = []
    for i in range(len(montharr)):
        if month == montharr[i]:
            month = str(i + 1)
    if int(month) < 10:
        month = '0' + month
    return year + month + date
    
    
def merge(arr, arr2, left, mid, right):
    
    n1 = mid - left + 1
    n2 = right - mid

    # Create temp arrays
    L = [0] * n1
    L2 = [0] * n1
    R = [0] * n2
    R2 = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[left + i]
        L2[i] = arr2[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
        R2[j] = arr2[mid + 1 + j]

    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = left  # Initial index of merged subarray

    # Merge the temp arrays back
    # into arr[left..right]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            arr2[k] = L2[i]
            i += 1
        else:
            arr[k] = R[j]
            arr2[k] = R2[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[],
    # if there are any
    while i < n1:
        arr[k] = L[i]
        arr2[k] = L2[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], 
    # if there are any
    while j < n2:
        arr[k] = R[j]
        arr2[k] = R2[j]
        j += 1
        k += 1

def merge_sort(arr, arr2, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, arr2, left, mid)
        merge_sort(arr, arr2, mid + 1, right)
        merge(arr, arr2, left, mid, right)


def binarySearch(arr, low, high, x):
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif int(arr[mid]) < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


filename = 'wordle.dat'
fh = open(filename, "r")          
num_arr = []
word_arr = []
My_dic = {}
Data_arr = [' ']*1038
for i in range(1038):
    tempvar = fh.readline()
    tempvar.strip()
    month, date, year, word = tempvar.split(' ')
    myData = mergeData(month, date, year)
    Data_arr[i] = myData + ' ' + word


for i in range(len(Data_arr)):
    Data_arr[i].strip()
    num, My_word = Data_arr[i].split(' ')
    num_arr.append(num)
    word_arr.append(My_word)



print("Welcome to the Wordle Database!")
n = 0

while n == 0:
    userInput = input("Enter w if you are looking for a word, or d for a word on a certain date: ")
    if userInput.lower() == 'd':
        merge_sort(num_arr, word_arr, 0, len(num_arr) - 1)
        print(num_arr)
        print(word_arr)
        Input_year = input("Enter the year: ")
        Input_month = input("Enter the month (3-letter abbreviation, as in 'Jan' for 'January'): ")
        Input_date = input("Enter the day: ")
        x = mergeData(month, date, year)
        x = int(x)    
#         if x <= 20210619:
#             print(f"{x} is too early. No wordles occurred before 20210619. Enter a later date.")
#         elif x >= 20240421:
#             print(f"{x} is too early. No wordles occurred before 20240421. Enter a ealier date.")
        result = binarySearch(num_arr, 0, len(num_arr)-1, x)
        print(f"The word entered on {num_arr[result]} was found {word_arr[result]}.")
    if userInput.lower() == 'w':
        merge_sort(word_arr, num_arr, 0, len(word_arr) - 1)
        
    if userInput.lower() == 'exit':
        n = 1

    
    


            
