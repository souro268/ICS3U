size = int(input("Please enter the size of your list: "))

n = 0
items = []
print("Enter your items now: ")
while n < size:
    inputs = input("Next item: ")
    items.append(inputs)
    n += 1
print(f"You habe entered {n} items.")
for x in range(len(items)):
    print(items[x])
    
