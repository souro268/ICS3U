import math as m

NormalNum = 10

# Correcting the header (removing the newline)
print("%3s|%5s|%7s|%5s" % ("N", "SQR", "Cubes", "Roots"))

# Loop to print the table
for i in range(10, 200, 15):
    two = int(m.pow(NormalNum, 2))  # Square of NormalNum, converted to int
    three = int(m.pow(NormalNum, 3))  # Cube of NormalNum, converted to int
    sqrt = m.sqrt(NormalNum)  # Square root of NormalNum, rounded to 2 decimal places
    # Printing the row (removed the extra newline)
    print("%3d|%5d|%7d|%5.2f" % (NormalNum, two, three, sqrt))
    NormalNum += 15  # Increment NormalNum by 15
