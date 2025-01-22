# Name: Sourish Keshari
# Student number: 904147@pdsb.net
# ICS 3U

# Variable Dictionary:
# filename: Name of the file containing Wordle data in a specific format
# fh: File handler to open and read the file
# num_arr: Array that stores Wordle puzzle dates as integers in YYYYMMDD format
# word_arr: Array that stores Wordle solutions as strings corresponding to the dates in num_arr
# Data_arr: Array to store formatted data from the file before splitting into num_arr and word_arr
# tempvar: Temporary variable to hold each line read from the file
# myData: String representing a formatted YYYYMMDD date generated from mergeData function
# month, date, year, word: Variables to temporarily hold data extracted from each line of the file
# n: Control variable for the User_Inputs function, keeps the loop running while n is 0

# Variable Dictionary:
# num_arr: List of integers representing Wordle puzzle dates in YYYYMMDD format.
# word_arr: List of strings containing the Wordle solutions corresponding to dates in num_arr.
# mergeData: Function that converts input date components (month, day, year) into YYYYMMDD format.
# merge_sort: Function that sorts two parallel arrays using the merge sort algorithm.
# binary_search: Function to perform binary search on a sorted array.
# n: Variable used as a flag to control the while loop in the User_Inputs function.

def User_Inputs(num_arr, word_arr, mergeData, merge_sort, binary_search, n):
    # Main user interaction loop for searching by word or date.
    while n == 0:
        print("****************************************************************************************************")
        print("Enter 'w' if you are looking for a word, 'd' if searching by date, and 'exit' to exit the program.")
        userInput = input("Enter your option: ")
        
        if userInput.lower() == 'd':
            # Sorting by date before binary search
            merge_sort(num_arr, word_arr, 0, len(num_arr) - 1)
            
            Input_year = input("Enter the year: ")
            if not Input_year.isdigit():
                print("Please enter a valid year and try again.\n")
                User_Inputs(num_arr, word_arr, mergeData, merge_sort, binary_search, 0)
            
            Input_month = input("Enter the month (3-letter abbreviation, e.g., 'Jan' for 'January'): ")
            if len(Input_month) > 3 or len(Input_month) < 3:
                print("Please enter a valid month abbreviation and try again.")
                User_Inputs(num_arr, word_arr, mergeData, merge_sort, binary_search, 0)
            
            Input_date = input("Enter the day: ")
            if not Input_date.isdigit():
                print("Please enter a valid date and try again.")
                User_Inputs(num_arr, word_arr, mergeData, merge_sort, binary_search, 0)
            
            if int(Input_date) < 10:
                # Padding single-digit dates with a leading zero
                Input_date = '0' + Input_date
            
            # Merging user input into YYYYMMDD format
            x = mergeData(Input_month, Input_date, Input_year)
            x = int(x)   
            result = binary_search(num_arr, 0, len(num_arr) - 1, x)
            
            if result is not None:
                print(f"The word '{word_arr[result]}' was the solution to the puzzle on {num_arr[result]}.")
            else:
                if x < 20210619:
                    print(f"{x} is too early. No Wordles occurred before 20210619. Enter a later date.")
                if x > 20240421:
                    print(f"{x} is too late. No Wordles occurred after 20240421. Enter an earlier date.")
            print("****************************************************************************************************")
        
        elif userInput.lower() == 'w':
            # Sorting by word before binary search
            merge_sort(word_arr, num_arr, 0, len(word_arr) - 1)
            Input_word = input("What word are you looking for? ").upper()
            result = binary_search(word_arr, 0, len(word_arr) - 1, Input_word)
            
            if result is not None:
                print(f"The word {word_arr[result]} was the solution to the puzzle on {num_arr[result]}")
            else:
                print(f"{Input_word} was not found in the database.")
            print("****************************************************************************************************")
        
        elif userInput.lower() == 'exit':
            print("Thank you for using this program.")
            print("****************************************************************************************************")
            return None
        
        else:
            # Invalid input handling
            print("Please try again and use a valid input.")
            print("****************************************************************************************************")
            User_Inputs(num_arr, word_arr, mergeData, merge_sort, binary_search, 0)

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

def merge(arr, arr2, left, mid, right):
    # Merges two sorted subarrays into a single sorted array.
    n1 = mid - left + 1
    n2 = right - mid
    L, L2 = [0] * n1, [0] * n1  # Temporary arrays for left subarray
    R, R2 = [0] * n2, [0] * n2  # Temporary arrays for right subarray
    
    for i in range(n1):
        L[i] = arr[left + i]
        L2[i] = arr2[left + i]
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

def merge_sort(arr, arr2, left, right):
    # Recursively sorts the array using the merge sort algorithm.
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, arr2, left, mid)
        merge_sort(arr, arr2, mid + 1, right)
        merge(arr, arr2, left, mid, right)

def binary_search(arr, low, high, x):
    # Searches for x in a sorted array using binary search.
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



try:
    filename = 'wordle.dat'  # The name of the file containing Wordle data
    fh = open(filename, "r")  # Opens the file for reading
    num_arr = []  # List to store puzzle dates in YYYYMMDD format
    word_arr = []  # List to store Wordle solutions
    Data_arr = [' '] * 1038  # Initializes array to store raw file data for 1038 entries

    for i in range(1038):  # Loops through each line in the file
        tempvar = fh.readline()  # Reads one line from the file
        tempvar.strip()  # Removes any leading/trailing whitespace
        try:
            # Splits the line into month, date, year, and word
            month, date, year, word = tempvar.split(' ')
        except:
            print("There is some error with the Wordle data in the file. Please try again.")
            continue  # Skips the faulty line and continues with the next iteration
        # Converts the month, date, and year into a single YYYYMMDD format string
        myData = mergeData(month, date, year)
        # Combines the formatted date with the word
        Data_arr[i] = myData + ' ' + word

    for i in range(len(Data_arr)):  # Processes formatted data
        Data_arr[i].strip()  # Removes leading/trailing whitespace from each entry
        # Splits each entry into date (num) and word
        num, My_word = Data_arr[i].split(' ')
        num = int(num)  # Converts date to integer format
        My_word = My_word.strip()  # Removes any extra whitespace from the word
        num_arr.append(num)  # Appends the date to num_arr
        word_arr.append(My_word)  # Appends the word to word_arr

    print("****************************************************************************************************")
    print("Welcome to the Wordle Database!")  # Welcome message
    n = 0  # Initializes the control variable for User_Inputs function
    # Calls the main user interaction function
    User_Inputs(num_arr, word_arr, mergeData, merge_sort, binary_search, n)
    fh.close()  # Closes the file after processing
except OSError as err:  # Handles file-related errors
    print("OS error:", err)
except ValueError:  # Handles data conversion errors
    print("Error with converting data to int, please try again.")
except Exception as err:  # Handles any other unexpected errors
    print(f"Unexpected {err=}, {type(err)=}")
