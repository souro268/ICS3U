import turtle as t
import math as m

def plotIT(x, y, thickness, color):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.dot(thickness, color)
                    

filename = "rocky_bullwinkle_mod.xpm"
fh = open(filename, "r")

colorData = fh.readline()
colorData = colorData.strip()

rows, cols, numColors = colorData.split()
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


thickness = 2
b = ( m.floor(cols/2) * thickness)
t.tracer(0,0)
for x in range(len(arr)):
    a = ( m.floor(rows/2) * thickness) *-1
    strtemp = arr[x].strip()
    print(strtemp)
    for l in range(len(strtemp)):
        plotIT(a, b, thickness, colorDefs[strtemp[l]])
        a = a + thickness
        if a == ((m.floor(rows/2)+1) * thickness):
            b = b - thickness
t.update()
                   
    

    
    
