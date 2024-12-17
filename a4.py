
'''
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
    
    
    
def bubble_sort_recursive(num, word_arr):
    
    for i in range(len(num)-1):
        if num[i] > num[i + 1]:
            temp = num[i]
            num[i] = num[i+1]
            num[i+1] = temp
            
            temp1 = word_arr[i]
            word_arr[i] = word_arr[i+1]
            word_arr[i+1] = temp1
    return
    
    
filename = 'wordle.dat'
fh = open(filename, "r")  # Opens the file in read mode
num = ['']*1038
word_arr = ['']*1038
for i in range(1038):
    tempvar = fh.readline()
    tempvar.strip()
    month, date, year, word = tempvar.split(' ')
    myData = mergeData(month, date, year)
    num[i] = str(myData)
    word_arr[i] = str(word)
    
    bubble_sort_recursive(num, word_arr)
#print(Data_Arr)
    
    

    


