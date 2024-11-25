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
Deletethis: Unnecessary data from the file's metadata.
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
    #Plots a dot at the given coordinates with specified thickness and color.
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.dot(thickness, color)

def Degrees0(plotIT):
    
    t.tracer(0, 0)
    b = cols / 2 * thickness
    for x in range(len(arr)):
        a = -rows / 2 * thickness
        strtemp = arr[x].strip()
        for l in range(len(strtemp)):
            color = colorDefs[strtemp[l]]
            plotIT(a, b, thickness, color)
            a += thickness
        b -= thickness
    t.update()

def Degrees90(plotIT):
    
    t.tracer(0, 0)
    b = cols / 2 * thickness
    for x in range(len(arr)):
        a = -rows / 2 * thickness
        strtemp = arr[x].strip()
        for l in range(len(strtemp)):
            color = colorDefs[strtemp[l]]
            plotIT(b, -a, thickness, color)
            a += thickness
        b -= thickness
    t.update()

def Degrees180(plotIT):
    
    t.tracer(0, 0)
    b = cols / 2 * thickness
    for x in range(len(arr)):
        a = -rows / 2 * thickness
        strtemp = arr[x].strip()
        for l in range(len(strtemp)):
            color = colorDefs[strtemp[l]]
            plotIT(-a, -b, thickness, color)
            a += thickness
        b -= thickness
    t.update()

def Degrees270(plotIT):
    
    t.tracer(0, 0)
    b = cols / 2 * thickness
    for x in range(len(arr)):
        a = -rows / 2 * thickness
        strtemp = arr[x].strip()
        for l in range(len(strtemp)):
            color = colorDefs[strtemp[l]]
            plotIT(-b, a, thickness, color)
            a += thickness
        b -= thickness
    t.update()

filename = "rb1.xpm"  # File containing image data
fh = open(filename, "r")  # Open the file for reading

colorData = fh.readline()
colorData.strip()  # Read and clean the first line of the file

rows, cols, numColors = colorData.split()  # Split metadata into variables
rows = int(rows)  # Convert rows to an integer
cols = int(cols)  # Convert columns to an integer
numColors = int(numColors)  # Convert the number of colors to an integer

colorDefs = {}  # Initialize a dictionary to store color mappings

temp = max(rows, cols)  # Use the larger dimension for array initialization
arr = [0] * temp  # Initialize an array for image data

for i in range(numColors):
    colorLine = fh.readline().strip()
    sym, c, color = colorLine.split()
    if sym == '~':  # Replace '~' with a space
        sym = " "
    colorDefs[sym] = color  # Map the symbol to its color

for j in range(temp):
    arr[j] = fh.readline()  # Read each row into the array
fh.close()  # Close the file

print("Number of columns: ", cols)
print("Number of rows: ", rows)
print("Number of colors: ", numColors)

thickness = int(input("Enter thickness: "))  # Prompt user for dot thickness
inputs = int(input("Enter the degree of rotation (0, 90, 180, 270): "))  # Prompt user for rotation degree

t.screensize(canvwidth=1000, canvheight=1000)  # Set up the canvas size

# Execute the appropriate function based on user input
if inputs == 0:
    Degrees0(plotIT)
elif inputs == 90:
    Degrees90(plotIT)
elif inputs == 180:
    Degrees180(plotIT)
elif inputs == 270:
    Degrees270(plotIT)
else:
    print("Invalid rotation degree. Please choose from 0, 90, 180, or 270.")
    n = 1
