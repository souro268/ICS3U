# Name : Sourish Keshari
# Student number: 904147
# ICS 3U 


import math as m

#1:
print("1")
print("********************************************************************************")
print("calculating the area of a rectangle.")
lengthR = float(input("Please enter the length of the rectangle: "))
wigthR = float(input("Please enter the wigth of the rectangle: "))


areaR = lengthR * wigthR
print("--------------------------------------------------------------------------------")
print("The area of the rectangle is: %.2f" % areaR)
print("--------------------------------------------------------------------------------")
 


#2
print("2")
print("********************************************************************************")
print("calculating the area of a circle.")
R = float(input("Please enter the radius of the circle: "))
areaC = m.pi * m.pow(R, 2)
print("--------------------------------------------------------------------------------")
print("The area is: %.2f" % areaC)
print("--------------------------------------------------------------------------------")



#3
print("3")
print("********************************************************************************")
print("calculating the volume of a cylinder.")
CylinderR = float(input("Please enter the radius of the cylinder: "))
CylinderH = float(input("Please enter the height of the cylinder: "))
volumeCy = m.pi * (m.pow(CylinderR, 2) * CylinderH)
print("--------------------------------------------------------------------------------")
print("The volume of the cylinder is %.2f" % volumeCy)
print("--------------------------------------------------------------------------------")
circle = 2 * (m.pi * m.pow(CylinderR, 2))
sides = 2 * m.pi * CylinderR * CylinderH
SA = circle + sides
print("--------------------------------------------------------------------------------")
print("The suface area of the cylinder is: %.2f" % SA)
print("--------------------------------------------------------------------------------")



#4
print("4")
print("********************************************************************************")
periodL = float(input("Please enter the length of the pendulum: "))
periodG = 9.8
sqrt = m.sqrt(periodL / periodG)
print("--------------------------------------------------------------------------------")
print("The time it takes for 1 swing will take %.2f" % (sqrt * (2 * m.pi)))
print("--------------------------------------------------------------------------------")
print("********************************************************************************")






