import math as m
arr = []
n = 0
print("Welcome to the school yearbook program!")
print(
while n == 0:
    perimeter = 0
    arr2 = []
    user = input("Input a number of photos: ")
    try:
        user = int(user)
        if user <= 0:
            print(f"{user} is not a valid number of photos. Please enter a positive number.")
        if user > 0:
            number = m.floor(m.sqrt(user))
            for x in range(1, number + 1):
                if number == m.sqrt(user):
                    arr.append(number)
                    arr.append(number)
                    break
                if user % x == 0:
                    arr.append(x)
            arr2 = arr[len(arr)-1:]
            perimeter = (arr2[0] + int(user/arr2[0])) * 2
            print(f"The best dimensions are {arr2[0]} x {int(user/arr2[0])} photos for a perimeter of {perimeter}.")
            print("----------------------------------------------------------------------------")
            print("")
    except:
        if user == "done" or user == "DONE" or user == "Done":
            print("Goodbye!")
            n = 1
    
    
    
