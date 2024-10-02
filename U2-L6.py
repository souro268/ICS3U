# Modify 1: Inverted right-angled triangle
# Prompting user for input on how many rows the triangle should have
n = int(input("Enter the number of rows for the first triangle: "))
print("Modify 1: Inverted Triangle")

# Loop to print inverted triangle
for i in range(n, 0, -1):  # Starts at n, decrements down to 1
    print("#" * i)  # Prints '#' multiplied by the current value of i

print("\nModify 2: Pyramid Shape")
# Modify 2: Pyramid Shape
# Prompting user for input on how many rows the pyramid should have
n = int(input("Enter the number of rows for the second triangle (pyramid): "))

# Loop to print pyramid
for i in range(1, n + 1):  # Starts at 1, increments up to n
    spaces = n - i  # Calculates the number of spaces for padding on the left
    hashes = 2 * i - 1  # Calculates the number of '#' characters to print
    print(" " * spaces + "#" * hashes)  # Prints spaces followed by hashes

print("\nModify 3: Diamond Shape")
# Modify 3: Diamond Shape
# Prompting user for input on how many rows the top half of the diamond should have
n = int(input("Enter the number of rows for the top half of the diamond: "))

# Top half of the diamond
for i in range(1, n + 1):  # Starts at 1, increments up to n
    spaces = n - i  # Calculates the number of spaces for the top half
    hashes = 2 * i - 1  # Calculates the number of '#' characters for the top half
    print(" " * spaces + "#" * hashes)  # Prints spaces followed by hashes

# Bottom half of the diamond
for i in range(n - 1, 0, -1):  # Starts at n-1, decrements down to 1
    spaces = n - i  # Calculates the number of spaces for the bottom half
    hashes = 2 * i - 1  # Calculates the number of '#' characters for the bottom half
    print(" " * spaces + "#" * hashes)  # Prints spaces followed by hashes
