import math as m

length = input("Enter the length of the of rectangle: ")
length = float(length)
Width = input("Enter the Width of the rectangle: ") 
Width = float(Width)

areaCircle = (m.pi * m.pow((length/2), 2)) / 2
areaRectangle = length * Width 
print("The area of the semi-circle is: ", areaCircle)
print("The area of the rectangle is:", areaRectangle, sep=" ")
print("Total area is: ", areaCircle + areaRectangle)
