

x = float(input("Please enter your mark: "))

if (x < 50) :
    print("F")
elif(x >= 50) and (x <= 59):
    print("D")
elif(x >= 60) and (x <= 69):
    print("C")
elif(x >= 70) and (x <= 79):
    print("B")
elif(x >= 80) and (x <= 100):
    print("A")
else:
    print("Please re-enter your mark")
