
'''
Oct 01 2023 BERET
Oct 02 2023 MERRY
Oct 03 2023 WHILE
Oct 04 2023 SPURT
Oct 05 2023 BUNCH
Oct 06 2023 CHIME
'''
def mergeData(month, date, year, word):
    month = month.lower()
    montharr = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    year_arr = []
    for i in range(len(montharr)):
        if month == montharr[i]:
            month = str(i + 1)
    if int(month) < 10:
        month = '0' + month
    return year + month + date
    
def bubblesort(Data_Arr)
    num = [0]*1038
    word = [0]*1038
    for i in range(len(Data_Arr)):
        num[i], word[i] = Data_Arr[i].strip()
    bubble_sort_recur(num, i, j, n, word)
    
    
def bubble_sort_recur(num, i, j, n, word):
    if j == n:
        i = i+1
        j = 0
    if i == n:
        return 
    if num[i] > num[j]:
        
        num[j], num[i] = num[i], num[j]
        word[j], word[i] = word[i], word[j]
        
        bubble_sort_recur(a, i, j+1, n, word);
    else:
        bubble_sort_recur(a, i, j+1, n, word);
    return num, word
    
    
filename = 'wordle.dat'
fh = open(filename, "r")  # Opens the file in read mode
Data_Arr = [0]*1038
for i in range(1038):
    tempvar = fh.readline()
    tempvar.strip()
    month, date, year, word =tempvar.split()
    myData = mergeData(month, date, year, word)
    Data_Arr[i] = myData + '-' + word
    
    

    



---------------------TEST

def bubble_sort_recur(num, i, j, n, word):
    if j == n:
        i = i+1
        j = 0
    if i == n:
        return 
    if num[i] > num[j]:
        
        num[j], num[i] = num[i], num[j]
        word[j], word[i] = word[i], word[j]
        
        bubble_sort_recur(a, i, j+1, n, word);
    else:
        bubble_sort_recur(a, i, j+1, n, word);
    return num, word

# Oct 03 2023 WHILE
# Oct 04 2023 SPURT
# Oct 05 2023 BUNCH
# Oct 06 2023 CHIME
# 
# 20231003 WHILE
# 20231004 SPURT
# 20231005 BUNCH
# 20231006 CHIME
num = [20231005, 20231006, 20231003, 20231004]
word = ['BUNCH', 'CHIME', 'WHILE', 'SPURT']

print(bubble_sort_recur(num, i, j, n, word))


--------------- BUBBLE SORT --------------------------
def bubble_sort_recursive(arr, n=None):
    # Initialize n as the length of the array for the first call
    if n is None:
        n = len(arr)
    
    # Base case: If the array size is 1, it is already sorted
    if n == 1:
        return
    
    # Perform one pass of the bubble sort
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            # Swap if the element is greater than the next
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    # Recursive call for the remaining array (excluding the last element)
    bubble_sort_recursive(arr, n - 1)

# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
bubble_sort_recursive(numbers)
print("Sorted array:", numbers)
