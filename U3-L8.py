# Not working
def strand1(one):
  z = 0
  for x in range(len(one)):
    if one[x] == "C" or "A" or "T" or "G":
      z += 1
    else:
      return(x)
  # return(len(one))
      
  
  
one = "CATGW"
print(strand1(one))
