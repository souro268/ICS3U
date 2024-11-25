import turtle as t
import math as m

def plotIT(x, y, thickness, color):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.dot(thickness, color)
                
def Degrees0(plotIT):
    t.tracer(0,0)
    b = cols/2 * thickness
    for x in range(len(arr)):
        a = -rows/2 * thickness
        strtemp = arr[x].strip()
        for l in range(len(strtemp)):
            color = colorDefs[strtemp[l]]
            plotIT(a, b, thickness, color)
            a = a + thickness
        b = b - thickness
    t.update()

def Degrees90(plotIT):
    t.tracer(0,0)
    b = cols/2 * thickness
    for x in range(len(arr)):
        a = -rows/2 * thickness
        strtemp = arr[x].strip()
        for l in range(len(strtemp)):
            color = colorDefs[strtemp[l]]
            plotIT(b, -a, thickness, color)
            a = a + thickness
        b = b - thickness
    t.update()

def Degrees180(plotIT):
    t.tracer(0,0)
    b = cols/2 * thickness
    for x in range(len(arr)):
        a = -rows/2 * thickness
        strtemp = arr[x].strip()
        for l in range(len(strtemp)):
            color = colorDefs[strtemp[l]]
            plotIT(-a, -b, thickness, color)
            a = a + thickness 
        b = b - thickness
    t.update()

def Degrees270(plotIT):
    t.tracer(0,0)
    b = cols/2 * thickness
    for x in range(len(arr)):
        a = -rows/2 * thickness
        strtemp = arr[x].strip()
        for l in range(len(strtemp)):
            color = colorDefs[strtemp[l]]
            plotIT(-b, a, thickness, color)
            a = a + thickness
        b = b - thickness
    t.update()

filename = "rb1.xpm"
fh = open(filename, "r")

colorData = fh.readline()
colorData = colorData.strip()

rows, cols, numColors, Deletethis = colorData.split()
rows = int(rows)
cols = int(cols)
numColors = int(numColors)

colorDefs = {}
temp = 0

if rows >= cols:
    temp = rows
if rows <= cols:
    temp = cols
arr = [0] * temp

for i in range(numColors):
    colorLine = fh.readline()
    colorLine = colorLine.strip()
    sym, c, color = colorLine.split()
    if sym == '~':
        sym = " "
    colorDefs[sym] = color

for j in range(temp):
    arr[j] = fh.readline()
fh.close()

print("Number of colums: ", cols)
print("Number of rows: ", rows)
print("Number of colors: ", numColors)

thickness = int(input("Enter thickness: "))
inputs = int(input("Enter the degree of rotation (0, 90, 180, 270): "))
t.screensize(canvwidth=1000, canvheight=1000)
if inputs == 0:
    Degrees0(plotIT)
elif inputs == 90:
    Degrees90(plotIT)
elif inputs == 180:
    Degrees180(plotIT)
elif inputs == 270:
    Degrees90(plotIT)

t.mainloop()
