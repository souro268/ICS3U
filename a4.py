
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
    for i in range(len(Data_Arr)):
        num, word = Data_Arr[i].strip()
    
        
    
    
filename = 'wordle.dat'
fh = open(filename, "r")  # Opens the file in read mode
Data_Arr = [0]*1038
for i in range(1038):
    tempvar = fh.readline()
    tempvar.strip()
    month, date, year, word =tempvar.split()
    myData = mergeData(month, date, year, word)
    Data_Arr[i] = myData + '-' + word
    
    

    
