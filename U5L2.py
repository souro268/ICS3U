filename = "file.txt"
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
for sym, color in colorDefs.items():
    print(f"{sym}: {color}")
for y in range(len(arr)):
    print(arr[y], end="")
