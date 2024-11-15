filename = "file.txt"
fh = open(filename, "r")

colorData = fh.readline()
colorData = colorData.strip()

rows, cols, numColors = colorData.split()
rows = int(rows)
cols = int(cols)
numColors = int(numColors)
#colorDefs = [[0] * 2] * numColors # declare the array
colorDefs = {}
arr = []
for i in range(numColors):
   colorLine = fh.readline()
   colorLine = colorLine.strip()
   sym, c, color = colorLine.split()
   if sym == '~':
       sym = " "
   colorDefs[sym] = color
   arr.append(colorDefs[sym])
fh.close()
space = " "
for sym, color in colorDefs.items():
    print(f"{sym}: {color}")

    

