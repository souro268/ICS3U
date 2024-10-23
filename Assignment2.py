# Name: Sourish Keshari
# Student number: 904147@pdsb.net
# ICS 3U

# Variable Dictionary:
# user: is the varible where the users' input is stored
# arr: is an array which stores all the factors of the number the user inters
# n: is a varible so the code runs forever until the user enters done which adds 1 to n, and when n is not 0 the program stops
# perimeter: is a varible where the perimeter is set to 0. (just to declare it)
# arr2: is another array to star the last value of the array which is the greatest common factor of the users number
# number: is a varible which stores the sqrt of the number and then floor function it to make the excution time smaller


import math as m
arr = []  # declares the array
n = 0  # decalares n as 0 so the program runs until the user enters done
print("Welcome to the school yearbook program!")  # printing text
print("Print 'Done' to exit the progran")  # printing text
while n == 0: # while loop which will run until user enters done which would thne set the number to  1 which would stop the look
    perimeter = 0 # declares the varible
    arr2 = [] # declares the array
    user = input("Input a number of photos (Must be a positive number): ") # asks for user input and sets the number to user
    try: # try function just in case
        user = int(user) # sets user input from string to int
        if user <= 0: # if input is less than or equal to 0 the number is invalue which
            print(f"{user} is not a valid number of photos. Please enter a positive number.")
        if user > 0: # if input ois vaild the program continews
            number = m.floor(m.sqrt(user)) # finds the sqrt and floor function of users number so its faster and easier 
            for x in range(1, number + 1): # for loop to find the factors of user input
                if number == m.sqrt(user): # if the number is a perfect square, the nuymber is added to the array
                    arr.append(number)
                    arr.append(number)
                    break # breaks the for loop and ends the factoing part
                if user % x == 0: # if the input is disible by x than add that number to the array
                    arr.append(x) # adds number to array
            arr2 = arr[len(arr)-1:] # removes all elements of the array besides the last one and sets it to arr2
            perimeter = (arr2[0] + int(user/arr2[0])) * 2 # finds perimeter
            print("----------------------------------------------------------------------------")
            print(f"The best dimensions are {arr2[0]} x {int(user/arr2[0])} photos for a perimeter of {perimeter}.") #prints the deminsions and perimeter
            print("----------------------------------------------------------------------------")
            
    except:
        if user == "done" or user == "DONE" or user == "Done": # if user input is done the program ends
            print("Goodbye!") 
            n = 1 # after user input is done, n is equal to 1 so the while loop doesnt work
