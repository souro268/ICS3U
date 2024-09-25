# Name: Sourish Keshari
# Student number: 904147@pdsb.net
# ICS 3U

# Variable Dictionary:
# lengthR: Length of the rectangle (unit)
# widthR: Width of the rectangle (unit)
# areaR: Area of the rectangle (unit²)
# R: Radius of the circle (unit)
# areaC: Area of the circle (unit²)
# CylinderR: Radius of the cylinder (unit)
# CylinderH: Height of the cylinder (unit)
# volumeCy: Volume of the cylinder (unit³)
# circle: Area of the cylinder's circular bases (unit²)
# sides: Lateral surface area of the cylinder (unit²)
# SA: Total surface area of the cylinder (unit²)
# periodL: Length of the pendulum (unit)
# periodG: Acceleration due to gravity (9.8 m/s²)
# sqrt: Square root used in pendulum calculation

import math as m  # Importing the math library 

# 1: Calculate the area of a rectangle
print("1")
print("********************************************************************************")
print("Calculating the area of a rectangle.")
lengthR = float(input("Please enter the length of the rectangle (unit): "))  # Get rectangle length from user
widthR = float(input("Please enter the width of the rectangle (unit): "))  # Get rectangle width from user

areaR = lengthR * widthR  # Calculate area of the rectangle
print("--------------------------------------------------------------------------------")
print("The area of the rectangle is: %.2f unit²" % areaR)  # Display the area of the rectangle
print("--------------------------------------------------------------------------------")

# 2: Calculate the area of a circle
print("2")
print("********************************************************************************")
print("Calculating the area of a circle.")
R = float(input("Please enter the radius of the circle (unit): "))  # Get circle radius from user
areaC = m.pi * m.pow(R, 2)  # Calculate area of the circle
print("--------------------------------------------------------------------------------")
print("The area is: %.2f unit²" % areaC)  # Display the area of the circle
print("--------------------------------------------------------------------------------")

# 3: Calculate the volume and surface area of a cylinder
print("3")
print("********************************************************************************")
print("Calculating the volume of a cylinder.")
CylinderR = float(input("Please enter the radius of the cylinder (unit): "))  # Get cylinder radius from user
CylinderH = float(input("Please enter the height of the cylinder (unit): "))  # Get cylinder height from user
volumeCy = m.pi * (m.pow(CylinderR, 2) * CylinderH)  # Calculate volume of the cylinder
print("--------------------------------------------------------------------------------")
print("The volume of the cylinder is: %.2f unit³" % volumeCy)  # Display the volume of the cylinder
print("--------------------------------------------------------------------------------")

circle = 2 * (m.pi * m.pow(CylinderR, 2))  # Calculate area of the cylinder's circular bases
sides = 2 * m.pi * CylinderR * CylinderH  # Calculate lateral surface area of the cylinder
SA = circle + sides  # Calculate total surface area of the cylinder
print("--------------------------------------------------------------------------------")
print("The surface area of the cylinder is: %.2f unit²" % SA)  # Display the surface area of the cylinder
print("--------------------------------------------------------------------------------")

# 4: Calculate the period of a pendulum
print("4")
print("********************************************************************************")
periodL = float(input("Please enter the length of the pendulum (unit): "))  # Get pendulum length from user
periodG = 9.8  # Acceleration due to gravity
sqrt = m.sqrt(periodL / periodG)  # Calculate the square root for pendulum period
print("--------------------------------------------------------------------------------")
print("The time it takes for 1 swing will take %.2f seconds" % (sqrt * (2 * m.pi)))  # Display the period of the pendulum in seconds
print("--------------------------------------------------------------------------------")
print("********************************************************************************")
