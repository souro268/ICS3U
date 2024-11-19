import turtle as t
import math as m

def plotIT(x, y, d, color):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.dot(d, color)
                    

filename = "temp.txt"
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

thickness = 5
a = (m.floor(rows/2) * -1) - (m.floor(rows/2) * thickness)
temp2 = a
b = m.floor(cols/2)  + (m.floor(cols/2) * thickness)

for x in range(len(arr)):
    strtemp = arr[x]
    for sym, color in colorDefs.items():
        print(strtemp)
        for l in range(len(strtemp)):
            if strtemp[l] == sym:
                plotIT(a, b, 3, color)
            a = a + thickness
            if a == temp2 * -1:
                b = b - thickness
            print(t.pos())

        
    

    
    
