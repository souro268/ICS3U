import random as r
def shuffle(A):
    # Precondition: A must be a 1D array
    #
    # Randomizes a list
    
    # add your code here!
    for x in range(0,len(A)-1):
        index = r.randint(0,len(A)-1)
        temp = A[x]
        A[x] = A[index]
        A[index] = temp
    
    return A
    
# driver code
B= [1,2,3,4,5,6,7]

inputs = int(input("Enter the size of your array: "))
for x in range(0, inputs):
    y = int(input(f"Enter number. You are at index {x+1}: "))
    B.append(y)
    
# compose the array with numbers from 1 to size, in order

# add your code here!

print(B) # before
B = shuffle(B)
print(B) # after
