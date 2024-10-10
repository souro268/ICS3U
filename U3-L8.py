def strand1(one):
    num = 0
    for a in range(len(one)):
        if one[a] == "C" or one[a] == "A" or one[a] == "T" or one[a] == "G":
            num = 0
        else:
            num += 1
            if (num >= 1):
                return f"Not valid: {one[a]} found in position {a + 1}"
    return "Valid"

one = input("Enter first strand: ")
print(strand1(one))
