# Sourish Keshari 904147
# ICS 3U


# Variable Dictionary:
# Exp_Mo: The expiration month of a credit card (integer or string input).
# Exp_Yr: The expiration year of a credit card (string input).
# month: A list of integers representing months (1 to 12).
# DateArr: List of expiration dates in YYYYMM format for credit cards.
# FirstNameArr: List of first names of cardholders.
# LastNameArr: List of last names of cardholders.
# CCtypeArr: List of credit card types (e.g., Visa, MasterCard).
# CCNumber: List of credit card numbers.
# Total_Name: Concatenation of a cardholder's first and last name.
# Status: Status of a credit card (EXPIRED, RENEW IMMEDIATELY, NOT EXPIRED).
# FileNameWriting: Name of the output file for sorted credit card data.
# FileWrite: File handle used to write output data.
# L, L2, L3, L4, L5: Temporary subarrays for the left half during merge sort.
# R, R2, R3, R4, R5: Temporary subarrays for the right half during merge sort.
# n1, n2: Sizes of the left and right subarrays in merge sort.
# left, mid, right: Indices used for dividing and merging in merge sort.

def Date(Exp_Mo, Exp_Yr):
    """
    Formats a credit card expiration date into YYYYMM format.
    - Exp_Mo: Expiration month as integer or string.
    - Exp_Yr: Expiration year as string.
    """
    Exp_Yr = str(Exp_Yr)  # Ensure the year is a string for concatenation.
    Exp_Mo = int(Exp_Mo)  # Convert the month to an integer.
    month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # List of all valid months.
    for x in month:  # Iterate over each valid month.
        if Exp_Mo < 10:  # If the month is a single digit (e.g., 1-9):
            if Exp_Mo == x:  # Check if the month matches the current month in the list.
                Exp_Mo = str(Exp_Mo)  # Convert the month to a string.
                Exp_Mo = '0' + Exp_Mo  # Add a leading zero (e.g., "01", "02").
                return Exp_Yr + Exp_Mo  # Return the formatted date as YYYYMM.
        if Exp_Mo >= 10:  # If the month is already two digits (e.g., 10-12):
            Exp_Mo = str(Exp_Mo)  # Convert the month to a string.
            return Exp_Yr + Exp_Mo  # Return the formatted date as YYYYMM.

def Comparison(DateArr, FirstNameArr, LastNameArr, CCtypeArr, CCNumber):
    """
    Compares credit card expiration dates and writes their status to a file.
    - DateArr: List of formatted expiration dates (YYYYMM).
    - FirstNameArr, LastNameArr: Cardholder names.
    - CCtypeArr: List of credit card types.
    - CCNumber: List of credit card numbers.
    """
    for x in range(len(DateArr)):  # Iterate over each credit card's data.
        Total_Name = FirstNameArr[x] + ' ' + LastNameArr[x] + ':'  # Combine full name.
        # Create formatted output with card details and expiration status.
        variable = "%-35s\t%-13s %s %s" % (Total_Name, CCtypeArr[x], '#' + CCNumber[x], DateArr[x])
        if DateArr[x] < 202501:  # Check if the card has expired.
            Status = ' EXPIRED'  # Mark card as expired.
            FileWrite.write(variable + Status + '\n')  # Write details to file.
        if DateArr[x] == 202501:  # Check if the card needs immediate renewal.
            Status = ' RENEW IMMEDIATELY'  # Mark card for immediate renewal.
            FileWrite.write(variable + Status + '\n')  # Write details to file.
        
    # Inform the user that sorting is complete.
    print(f"You sorting is done! Please open the file called '{FileNameWriting}' on you computer to view the output! :D")

def merge(arr, arr2, arr3, arr4, arr5, left, mid, right):
    """
    Merges two sorted subarrays into a single sorted array.
    - arr, arr2, arr3, arr4, arr5: Arrays of data to sort.
    - left, mid, right: Indices for splitting and merging.
    """
    for x in range(len(arr)):
        arr[x] = int(arr[x])  # Ensure main array elements are integers.
    n1 = mid - left + 1  # Size of the left subarray.
    n2 = right - mid  # Size of the right subarray.
    # Temporary arrays for the left and right halves.
    L, L2, L3, L4, L5 = [0] * n1, [0] * n1, [0] * n1, [0] * n1, [0] * n1
    R, R2, R3, R4, R5 = [0] * n2, [0] * n2, [0] * n2, [0] * n2, [0] * n2
    
    # Copy data into the left temporary arrays.
    for i in range(n1):
        L[i] = arr[left + i]
        L2[i] = arr2[left + i]
        L3[i] = arr3[left + i]
        L4[i] = arr4[left + i]
        L5[i] = arr5[left + i]       
        
    # Copy data into the right temporary arrays.
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
        R2[j] = arr2[mid + 1 + j]
        R3[j] = arr3[mid + 1 + j]
        R4[j] = arr4[mid + 1 + j]
        R5[j] = arr5[mid + 1 + j]
    
    # Merge the temporary arrays back into the main arrays.
    i = j = 0
    k = left
    while i < n1 and j < n2:  # Compare elements from both subarrays.
        if L[i] <= R[j]:
            # If the left element is smaller, add it to the main array.
            arr[k], arr2[k], arr3[k], arr4[k], arr5[k] = L[i], L2[i], L3[i], L4[i], L5[i]
            i += 1
        else:
            # If the right element is smaller, add it to the main array.
            arr[k], arr2[k], arr3[k], arr4[k], arr5[k] = R[j], R2[j], R3[j], R4[j], R5[j]
            j += 1
        k += 1
    
    # Copy any remaining elements from the left subarray.
    while i < n1:
        arr[k], arr2[k], arr3[k], arr4[k], arr5[k] = L[i], L2[i], L3[i], L4[i], L5[i]
        i += 1
        k += 1
    
    # Copy any remaining elements from the right subarray.
    while j < n2:
        arr[k], arr2[k], arr3[k], arr4[k], arr5[k] = R[j], R2[j], R3[j], R4[j], R5[j]
        j += 1
        k += 1

def merge_sort(arr, arr2, arr3, arr4, arr5, left, right):
    """
    Recursively sorts the array using the merge sort algorithm.
    - arr, arr2, arr3, arr4, arr5: Arrays of data to sort.
    - left, right: Indices defining the range of the array to sort.
    """
    if left < right:  # Base case: Stop if the array has only one element.
        mid = (left + right) // 2  # Find the midpoint of the array.
        merge_sort(arr, arr2, arr3, arr4, arr5, left, mid)  # Sort the left half.
        merge_sort(arr, arr2, arr3, arr4, arr5, mid+1, right)  # Sort the right half.
        merge(arr, arr2, arr3, arr4, arr5, left, mid, right)  # Merge sorted halves.

# Initialize variables for file input/output.
filename = 'data.dat'  # The name of the file containing Wordle data.
fh = open(filename, "r")  # Open the input file for reading.

FileNameWriting = 'Sorted_data.txt'  # Name of the output file.
FileWrite = open(FileNameWriting, 'w')  # Open the output file for writing.

# Initialize arrays to hold data from the file.
FirstNameArr = []
LastNameArr = []
CCtypeArr = []
CCNumber = []
DateArr = []
n = 1

# Read and process each line from the input file.
Temp_File_Line = fh.readline()  # Read the header line.
while n == 1:  # Loop until all lines are read.
    try:
        tempvar = fh.readline()  # Read one line from the file.
    except:
        # Handle file reading errors.
        print("There is an error with reading the file. Please try again.")
        n = 0
    tempvar.strip()  # Remove any leading/trailing whitespace.
    try:
        # Split the line into individual fields and store them.
        First_Name, Last_Name, CC_Type, CC_Number, Exp_Mo, Exp_Yr = tempvar.split(',')
        FirstNameArr.append(First_Name.strip())
        LastNameArr.append(Last_Name.strip())
        CCtypeArr.append(CC_Type.strip())
        CCNumber.append(CC_Number.strip())
        temp = Date(Exp_Mo, Exp_Yr.strip())  # Format the expiration date.
        DateArr.append(temp)
    except ValueError:
        # Handle errors when splitting fields.
        n = 0
    except Exception as err:  # Catch any other unexpected errors.
        print(f"There has been an error. Error message: {err=}. Error type: {type(err)=}")
        n = 0

# Sort and compare credit card data.
merge_sort(DateArr, FirstNameArr, LastNameArr, CCtypeArr, CCNumber, 0, len(DateArr) - 1)
Comparison(DateArr, FirstNameArr, LastNameArr, CCtypeArr, CCNumber)

# Close the input and output files.
fh.close()
FileWrite.close()
