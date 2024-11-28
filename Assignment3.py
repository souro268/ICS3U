'''
Name: Sourish Keshari
Student number: 904147@pdsb.net
ICS 3U

Variable Dictionary:
plotIT: Draws a dot at a specific location on the screen with a given thickness and color.
Degrees0: Draws the image in its original orientation (0-degree rotation).
Degrees90: Rotates the image 90 degrees clockwise and draws it.
Degrees180: Rotates the image 180 degrees clockwise and draws it.
Degrees270: Rotates the image 270 degrees clockwise and draws it.
filename: Stores the name of the file containing the image data ("rb1.xpm").
fh: File handle for reading data from the file.
colorData: First line of the file containing image metadata (rows, columns, and colors).
rows: Number of rows in the image.
cols: Number of columns in the image.
numColors: Total number of unique colors in the image.
colorDefs: Dictionary mapping symbols to their respective colors.
temp: Stores the larger value between rows and columns (for array initialization).
arr: List storing the image's pixel data as strings of symbols.
colorLine: Temporary string for storing a line that defines a color in the file.
sym: Symbol representing a specific color in the image.
c: Placeholder for unused data in the color definition line.
color: Hexadecimal color code (e.g., "#RRGGBB") associated with a symbol.
thickness: User-defined thickness of the dots.
inputs: User input specifying the degree of rotation (0, 90, 180, or 270).
'''

import turtle as t
import math as m

def plotIT(x, y, thickness, color):
    #Plots a dot at the given coordinates with specified thickness and 
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.shape('square')
    t.color(color)
    t.turtlesize(thickness, thickness)
    t.stamp()
    t.penup()

def RotationFunction(plotIT, rotation):
    
    t.tracer(0, 0)
    b = (cols / 2 * thickness)
    for x in range(0, len(arr), 1):
        strtemp = ''
        a = (rows / 2 * thickness) * -1
        strtemp = arr[x].strip()
        b -= thickness
        for l in strtemp:
            color = colorDefs[l]
            if rotation == 0:
                plotIT(a, b, thickness, color)
            if rotation == 90:
                plotIT(b, -a, thickness, color)
            if rotation == 180:
                plotIT(-a, -b, thickness, color)
            if rotation == 270:
                plotIT(-b, a, thickness, color)
            a += thickness
    t.update()

def ForLoops(fh, numColors, temp, RotationFunction):
    for i in range(numColors):
        colorLine = fh.readline().strip()
        sym, c, color = colorLine.split()
        if sym == '~':  # Replace '~' with a space
            sym = " "
        colorDefs[sym] = color  # Map the symbol to its color

    for j in range(temp):
        arr[j] = fh.readline()  # Read each row into the array
    RotationFunction(plotIT, rotation)



#filename = "rocky_bullwinkle_mod.xpm"  # File containing image data
filename = 'smiley_emoji_mod.xpm'
#filename = 'file.txt'
fh = open(filename, "r")  # Open the file for reading

colorData = fh.readline()
colorData.strip()  # Read and clean the first line of the file

rows, cols, numColors = colorData.split()  
rows = int(rows)  # Convert rows to an integer
cols = int(cols)  # Convert columns to an integer
numColors = int(numColors)  # Convert the number of colors to an integer

colorDefs = {}  # Initialize a dictionary to store color mappings

temp = max(rows, cols)  # Use the larger dimension for array initialization
arr = [0] * temp  # Initialize an array for image data

thickness = int(input("Enter thickness: "))  # Prompt user for dot thickness
inputs = int(input("Enter the degree of rotation (0, 90, 180, 270): "))  # Prompt user for rotation degree
print("Check your taskbar to open the turtle graphics window to view your image")

t.screensize(canvwidth=1000, canvheight=1000)  # Set up the canvas size
# Execute the appropriate function based on user input
if inputs == 0:
    rotation = 0
    ForLoops(fh, numColors, temp, RotationFunction)
elif inputs == 90:
    rotation = 90
    ForLoops(fh, numColors, temp, RotationFunction)
elif inputs == 180:
    rotation = 180
    ForLoops(fh, numColors, temp, RotationFunction)
elif inputs == 270:
    rotation = 270
    ForLoops(fh, numColors, temp, RotationFunction)
else:
    print("Invalid rotation degree. Please choose from 0, 90, 180, or 270.")

t.goto(0, 0)
t.dot(10, 'purple')
print("Number of columns: ", cols)
print("Number of rows: ", rows)
print("Number of colors: ", numColors)
fh.close()  # Close the file


