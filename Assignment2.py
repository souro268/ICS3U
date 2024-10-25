# Name: Sourish Keshari
# Student number: 904147@pdsb.net
# ICS 3U

# Variable Dictionary:
# user: variable that stores the user's input
# arr: an array that stores all the factors of the number the user enters
# n: variable that keeps the code running indefinitely until the user enters "done," which increments n, stopping the program when n is not 0
# perimeter: variable initialized to 0 to declare the perimeter value
# arr2: another array to store the last value of arr, which is the greatest factor of the user's number
# number: variable that stores the square root of the number, floored to reduce execution time

import math as m

def factors(user):  # defines a function to find the factors of a number
    number = m.floor(m.sqrt(user))  # finds the floored square root of the user's number for faster processing
    for x in range(1, number + 1):  # loop to find factors of the user input
        if number == m.sqrt(user):  # if the number is a perfect square, it is added twice to the array
            arr.append(number)
            arr.append(number)
            return arr
        if user % x == 0:  # if user input is divisible by x, add x to the array
            arr.append(x)  # adds factor to the array
    return arr

arr = []  # declares the array
n = 0  # initializes n to 0 to keep the program running until the user enters "done"
print("Welcome to the school yearbook program!")  # introductory message
print("Enter 'Done' to exit the program")  # exit instruction

while n == 0:  # loop that runs until user enters "done," setting n to 1 and stopping the loop
    perimeter = 0  # initializes the perimeter variable
    arr2 = []  # declares arr2 as an empty array
    user = input("Input a number of photos (must be a positive number): ")  # prompts user for input

    try:  # try block for input validation
        user = int(user)  # converts user input from string to integer
        if user <= 0:  # if input is 0 or negative, prompt user to enter a positive number
            print(f"{user} is not a valid number of photos. Please enter a positive number.")
        if user > 0:  # if input is valid, continue program
            arr = factors(user)
            arr2 = arr[len(arr)-1:]  # keeps only the last element of arr as arr2
            perimeter = (arr2[0] + int(user / arr2[0])) * 2  # calculates the perimeter
            print("----------------------------------------------------------------------------")
            print(f"The best dimensions are {arr2[0]} x {int(user / arr2[0])} photos for a perimeter of {perimeter}.")
            print("----------------------------------------------------------------------------")
            
    except:
        if user.lower() == "done":  # if user input is "done" (case-insensitive), end program
            print("Goodbye!")
            n = 1  # sets n to 1, stopping the while loop
