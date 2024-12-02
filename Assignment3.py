'''
Name: Sourish Keshari
Student number: 904147@pdsb.net
ICS 3U

plotIT: Draws a dot at a specific location on the screen with a given thickness and color.
rotation: Specifies the degree of rotation for the image (0, 90, 180, or 270).
RotationFunction: Handles the rotation of the image based on the specified degree and draws it.
b: Tracks the vertical position on the canvas, adjusted by the dot's thickness.
arr: An array that stores the pixel data of the image (rows of symbols).
strtemp: A temporary string to hold a row of pixel data as it's processed.
a: Tracks the horizontal position on the canvas.
colorDefs: A dictionary mapping symbols (characters) to their corresponding colors.
fh: File handle used to read the image data from the file.
filename: Stores the name of the file containing the image data (e.g., "smiley_emoji_mod.xpm").
colorData: The first line of the file containing image metadata, including rows, columns, and colors.
rows: The number of rows in the image.
cols: The number of columns in the image.
numColors: The total number of unique colors in the image.
temp: The larger of the number of rows or columns, used to initialize the array.
inputs: The degree of rotation input by the user (0, 90, 180, or 270).
thickness: The thickness of the dots, specified by the user.
'''

import turtle as t  # Importing the turtle module for drawing graphical representations

# Function to plot a dot at specified coordinates with given thickness and color
def plotIT(x, y, thickness, color):
    t.penup()  # Lifts the pen to move without drawing
    t.goto(x, y)  # Moves to the specified (x, y) coordinates
    t.pendown()  # Lowers the pen to enable drawing
    t.dot(thickness, color)  # Draws a dot of the given thickness and color

# Function to handle rotations of the image based on the degree of rotation specified
def RotationFunction(plotIT, rotation):
    t.tracer(0, 0)  # Turns off animation to speed up drawing
    b = (cols / 2 * thickness)  # Initializes b as half the canvas height in thickness units
    for x in range(0, len(arr)):  # Iterates through each row of the image
        strtemp = ''  # Temporary string to hold the row's pixel data
        a = (rows / 2 * thickness) * -1  # Initializes a to the topmost point of the canvas
        strtemp = arr[x].strip()  # Removes any whitespace from the row data
        b = b - (thickness * 1)  # Moves one row up for each iteration
        for l in range(len(strtemp)):  # Iterates through each pixel in the row
            color = colorDefs[strtemp[l]]  # Retrieves the color corresponding to the symbol
            # Checks the rotation and plots the pixel accordingly
            if rotation == 0:
                plotIT(a, b, thickness, color)  # Plots the original orientation
            if rotation == 90:
                plotIT(b, -a, thickness, color)  # Plots rotated 90 degrees clockwise
            if rotation == 180:
                plotIT(-a, -b, thickness, color)  # Plots rotated 180 degrees clockwise
            if rotation == 270:
                plotIT(-b, a, thickness, color)  # Plots rotated 270 degrees clockwise
            a = a + (thickness * 1)  # Moves to the next column in the row
    t.update()  # Updates the drawing on the screen

# Function to process the file data and draw the image
def ForLoops(fh, numColors, temp, RotationFunction):
    for i in range(numColors):  # Loops through the number of unique colors
        colorLine = fh.readline().strip()  # Reads and cleans each line defining a color
        sym, c, color = colorLine.split()  # Splits the line into symbol, placeholder, and color
        if sym == '~':  # Checks for the tilde symbol and replaces it with a space
            sym = " "
        colorDefs[sym] = color  # Maps the symbol to its corresponding color

    for j in range(temp):  # Loops through the maximum of rows and columns
        arr[j] = fh.readline()  # Reads and stores each row of pixel data
    RotationFunction(plotIT, rotation)  # Calls the RotationFunction to draw the image

# Specifies the filename of the XPM file to be read
filename = 'smiley_emoji_mod.xpm'
fh = open(filename, "r")  # Opens the file in read mode

colorData = fh.readline()  # Reads the first line containing metadata
colorData.strip()  # Cleans any extra whitespace from the metadata

# Parses the metadata to extract rows, columns, and the number of colors
rows, cols, numColors = colorData.split()  
rows = int(rows)  # Converts the number of rows to an integer
cols = int(cols)  # Converts the number of columns to an integer
numColors = int(numColors)  # Converts the number of colors to an integer

colorDefs = {}  # Initializes a dictionary to store symbol-to-color mappings
temp = max(rows, cols)  # Finds the larger dimension for initializing the array
arr = [0] * temp  # Creates an array to store image pixel data

thickness = int(input("Enter thickness: "))  # Asks the user for the dot thickness
# Asks the user for the rotation degree (0, 90, 180, or 270)
inputs = int(input("Enter the degree of rotation (0, 90, 180, 270): "))
print("Check your taskbar to open the turtle graphics window to view your image")

t.screensize(canvwidth=1000, canvheight=1000)  # Sets the turtle canvas size

# Handles the user-selected rotation and calls the ForLoops function to draw
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

print("Number of columns: ", cols)  # Displays the number of columns in the image
print("Number of rows: ", rows)  # Displays the number of rows in the image
print("Number of colors: ", numColors)  # Displays the number of unique colors
fh.close()  # Closes the file after reading
