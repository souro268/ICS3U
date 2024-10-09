def DNA(strand):
  z = ""
  for x in range(len(strand)):
    
    if strand[x] == ("C"):
      output.append("G")
      
    if strand[x] == ("G"):
      output.append("C")
      
    if strand[x] == ("A"):
      output.append("T")
      
    if strand[x] == ("T"):
      output.append("A")
    z = z + output[x]
  return z
output = []
strand = input("Enter strand: ")
print(DNA(strand))


