

def User_Inputs(num_arr, word_arr, mergeData, merge_sort, binary_search, n):
    
    while n == 0:
        userInput = input("Enter w if you are looking for a word, or d for a word on a certain date: ")
        if userInput.lower() == 'd':
            merge_sort(num_arr, word_arr, 0, len(num_arr) - 1)
            
            Input_year = input("Enter the year: ")
            if not Input_year.isdigit():
                print("Please enter a valid year and try again.\n")
                User_Inputs(num_arr, word_arr, mergeData, merge_sort, binary_search, 0)
            Input_month = input("Enter the month (3-letter abbreviation, as in 'Jan' for 'January'): ")
            if len(Input_month) > 3 or len(Input_month) < 3:
                print("Please enter a valid month abbreviation and try again.\n")
                User_Inputs(num_arr, word_arr, mergeData, merge_sort, binary_search, 0)
            Input_date = input("Enter the day: ")
            if not Input_date.isdigit():
                print("Please enter a valid date and try again.\n")
                User_Inputs(num_arr, word_arr, mergeData, merge_sort, binary_search, 0)
            if int(Input_date) < 10:
                Input_date = '0' + Input_date
            x = mergeData(Input_month, Input_date, Input_year)
            x = int(x)   
            result = binary_search(num_arr,0, len(num_arr)-1, x)
            if result is not None:
                print(f"The word '{word_arr[result]}' was found at position {num_arr[result]}.\n")
            else:
                if(x < 20210619):
                    print(f"{x} is too early. No wordles occurred before 20210619. Enter a later date.\n")
                if(x > 20240421):
                    print(f"{x} is too late. No wordles occurred after 20240421. Enter a earlier date.\n")                
                
        if userInput.lower() == 'w':
            merge_sort(word_arr, num_arr, 0, len(word_arr) - 1)
            Input_word = input("What word are you looking for? ")
            Input_word = Input_word.upper()
            result = binary_search(word_arr,0, len(word_arr)-1, Input_word)
            if result is not None:
                print(f"The word {word_arr[result]} was the solution to the puzzle on {num_arr[result]}\n")
            if result is None:
                print(f"{Input_word} was not found in the database.\n")
            
        if userInput.lower() == 'exit':
            print("Thank you for using this program.\n")
            n = 1
        if not userInput.lower() == 'w' and not userInput.lower() == 'd' and not userInput.lower() == 'exit':
            print("Please try again and use a valid input.\n")
            User_Inputs(num_arr, word_arr, mergeData, merge_sort, binary_search, 0)

def mergeData(month, date, year):
    month = month.lower()
    month_arr = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    year_arr = []
    try:
        for i in range(len(month_arr)):
            if month == month_arr[i]:
                month = str(i + 1)
        if int(month) < 10:
            month = '0' + month
        return year + month + date
    except:
        print("Please enter a valid month and try again.\n")
        User_Inputs(num_arr, word_arr, mergeData, merge_sort, binary_search, 0)
    
    
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


def binary_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return None


            
            
filename = 'wordle.dat'
fh = open(filename, "r")          
num_arr = []
word_arr = []
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
    num = int(num)
    My_word = My_word.strip()
    num_arr.append(num)
    word_arr.append(My_word)



print("Welcome to the Wordle Database!")
n = 0
User_Inputs(num_arr, word_arr, mergeData, merge_sort, binary_search, n)
fh.close()


    
    


            
