# Ask the user to enter a positive integer
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop to go through each row
while row < size:
    # Use for loop to print stars in each column
    for col in range(size):
        print("*", end="")
    # Move to the next line after finishing a row
    print()
    row += 1
