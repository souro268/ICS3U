import math as m
lists = []
inputs = int(input("Please enter a integer thats >= 3: ")) # asks user for input

if inputs >= 3: # checks if input is >= to 3
    for n in range(3,inputs + 1, 1): 
        if(n%2 == 1):  # checks if the number of odd
            a = m.pow(n,2) # math sutff
            b = m.pow((m.floor(n/2)) * (n+1),    2) # math sutff
            c = m.pow((m.floor(n/2)) * (n+1) + 1,2)   # math sutff
            total = a+b # math sutff
            if total == c: # checks if a + b(total) is equal to c, if so that means its a triple
                lists.append(n) # adds n to the list of numbers so you know the starting
                print(f"A = {m.sqrt(a)} \nB = {m.sqrt(b)} \nC = {m.sqrt(c)} \ntotal = {m.sqrt(total)}") # prints the values
                print("----------------------------------------------")
        elif(n%2 == 0): # checks if the number is even
            z = m.pow(n,2)/4 # math sutff
            a1 = m.pow(n,2) # math sutff
            b1 = m.pow(z - 1, 2) # math sutff
            c1 = m.pow(z + 1, 2) # math sutff
            total1 = a1+b1 # math sutff
            if total1 == c1: # checks if total (a+b) is equal to c
                lists.append(n) # adds n to the list of numbers so you know the starting
                print(f"A = {m.sqrt(a1)} \nB = {m.sqrt(b1)} \nC = {m.sqrt(c1)} \ntotal = {m.sqrt(total1)}") # prints the values
                print("----------------------------------------------")
    print(lists)
else: # if the number is less than 3 then it tells the user to enter a value above 3
    print("Please enter a value above 3") # prints

        
