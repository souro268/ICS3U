
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
    
    
def merge_sort(num_arr, word_arr):
    if len(num_arr) <= 1:
        return num_arr, word_arr

    mid = len(num_arr) // 2
    left_num, left_word = merge_sort(num_arr[:mid], word_arr[:mid])
    right_num, right_word = merge_sort(num_arr[mid:], word_arr[mid:])

    i = j = 0
    sorted_num_arr = []
    sorted_word_arr = []

    while i < len(left_num) and j < len(right_num):
        if left_num[i] <= right_num[j]:
            sorted_num_arr.append(left_num[i])
            sorted_word_arr.append(left_word[i])
            i += 1
        else:
            sorted_num_arr.append(right_num[j])
            sorted_word_arr.append(right_word[j])
            j += 1

    sorted_num_arr.extend(left_num[i:])
    sorted_word_arr.extend(left_word[i:])
    sorted_num_arr.extend(right_num[j:])
    sorted_word_arr.extend(right_word[j:])

    # add the data to dictionary
    return sorted_num_arr, sorted_word_arr


def Seach_by_Date(Input_year, Input_month, Input_date):
    
    found_date = None 
    found_word = None

    found_num = mergeData(Input_month, Input_date, Input_year)
    temp = found_date
    for keys, values in My_dic.items():
        if values == found_num:   
            found_date = values
            found_word = keys
            break
    if found_word is not None:
        return found_date, found_num, temp
    else:
        temp2, found_date = list(My_dic.items())[-1]
        return None, found_date, temp
    
filename = 'wordle.txt'
fh = open(filename, "r")  

My_dic = {}
Data_arr = [' ']*1038
for i in range(1038):
    tempvar = fh.readline()
    tempvar.strip()
    month, date, year, word = tempvar.split(' ')
    myData = mergeData(month, date, year)
    Data_arr[i] = myData + ' ' + word
    
num_arr = []
word_arr = []

for i in range(len(Data_arr)):
    Data_arr[i].strip()
    num, My_word = Data_arr[i].split(' ')
    num_arr.append(num)
    word_arr.append(My_word)

merge_sort(num_arr, word_arr)
print(f"{num_arr} + {word_arr}")
print("Welcome to the Wordle Database!")
n = 0

while n == 0:
    userInput = input("Enter w if you are looking for a word, or d for a word on a certain date: ")
    if userInput.lower() == 'd':
        Input_year = input("Enter the year: ")
        Input_month = input("Enter the month (3-letter abbreviation, as in 'Jan' for 'January'): ")
        Input_date = input("Enter the day: ")
        found_date, found_word, temp = Seach_by_Date(Input_year, Input_month, Input_date)
        if found_word is not None:
            print(f"The word entered on {found_date} was {found_word}.")
        else:
            print(f"{temp} is too early. No wordles occurred before {found_word}. Enter a later date.")
    
    if userInput.lower() == 'exit':
        n = 1
    


            
