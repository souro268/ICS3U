import math as m
lists = []
inputs = int(input("Please enter a integer thats >= 2: ")) # asks user for input

if inputs >= 2: # checks if input is >= to 2 
    for n in range(3,inputs + 1, 1): # forloop that starts at 1
        if(n%2 == 1):  # checks if the number of odd
            a = m.pow(n,2) # math stuff
            b = m.pow((m.floor(n/2)) * (n+1),    2) # math stuff
            c = m.pow((m.floor(n/2)) * (n+1) + 1,2)   # math stuff
            total = a+b # math sutff
            if total == c: # checks if a + b(total) is equal to c, if so that means its a triple
                lists.append(n) # adds n to the list of numbers so you know the starting
                a = m.sqrt(a)
                b = m.sqrt(b)
                c = m.sqrt(c)
                total = m.sqrt(total)
                print("A: %d, B: %d, C: %d" % (a, b, c))
                print("----------------------------------------------") # prints
        elif(n%2 == 0): # checks if the number is even
            z = m.pow(n,2)/4 # math stuff
            a1 = m.pow(n,2) # math stuff
            b1 = m.pow(z - 1, 2) # math stuff
            c1 = m.pow(z + 1, 2) # math stuff
            total1 = a1+b1 # math stuff
            if total1 == c1: # checks if total (a+b) is equal to c
                lists.append(n) # adds n to the list of numbers so you know the starting
                a1 = m.sqrt(a1)
                b1 = m.sqrt(b1)
                c1 = m.sqrt(c1)
                total1 = m.sqrt(total1)
                print("A: %d, B: %d, C: %d" % (a1, b1, c1))
                print("----------------------------------------------") # prints
    print(lists)
else: # if the number is less than 2 then it tells the user to enter a value above 2
    print("Please enter a value above 2") # prints

        
