import math as m

# Function to factorize a number and return proper factors
def factorize(x):
    factors = []
    i = m.floor(m.sqrt(x))  # Get the square root of x for optimization
    for j in range(1, i+1):  # Iterate from 1 to the square root of x
        if x % j == 0 and x % j != x:  # Check if j is a proper factor
            factors.append(j)
        if x // j != j and x // j != x:  # Add the corresponding factor if it's not a duplicate
            factors.append(x // j)
    factors.sort()  # Sort the factors
    return factors

# Function to check if the sum of the factors classifies the number as abundant, perfect, or deficient
def check(factors, num):
    total_sum = 0
    for factor in factors:
        total_sum += factor
    if total_sum > num:  # Abundant if the sum is greater than the number
        return ["abundant", total_sum]
    elif total_sum == num:  # Perfect if the sum equals the number
        return ["perfect", total_sum]
    else:  # Deficient if the sum is less than the number
        return ["deficient", total_sum]

# Main program loop
print("Proper factors!")
print("------------------------------")
number = 1
while number == 1:
    # Get user input for the number
    fac = int(input("Please enter a number: "))
    
    # Factorize the number and check its classification
    fact = factorize(fac)
    result = check(fact, fac)
    factor_sum = result[1]
    status = result[0]
    
    # Print the results
    print(f"Factor sum: {factor_sum}")
    print(f"The number {fac} is {status}")
    
    # Ask the user if they want to repeat the process
    repeat = input("Would you like to go again? (Y/N): ")
    if repeat == 'y':
        number = 1
    elif repeat == 'Y':
        number = 1
    else:
        number += 1
        print("Thank you for playing!")
