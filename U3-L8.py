def validate(s):
    num = 0
    for a in range(len(s)):
        if s[a] == "C" or s[a] == "A" or s[a] == "T" or s[a] == "G":
            num = 0
        else:
            num += 1
            if (num >= 1):
                return f"Not valid: {s[a]} found in position {a + 1}"
    return "Valid"

s = input("Enter first strand: ")
print(validate(s))
