ar2 = [[3, 4, 1, 2, 6],
      [9, 2, 3, 7, 5],
      [4, 2, 1, 0, 3]]

for i in range(len(ar2)):
  ar3 = ar2[i]
  total = 0
  for j in range(len(ar3)):
      print(ar3[j], end=" ")
      total += ar3[j] 
  print("Total =", total)
  print() # PREDICT A
print(ar2) # PREDICT B

# First I tried to add up everything using a1 + a2 ... a5 but that didnt work beucase after each iteration it would cahnge.
# My next idea was to have total = total + ar[j] which would add the next index in the array to total. after the second for loop
# if done, total would reset 
