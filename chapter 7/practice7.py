"""7. Write a program to print the following star pattern.
  *
 ***
***** for n = 3
"""
# Input the number of rows
n = int(input("Enter the number of rows (n): "))

# Loop for each row
for i in range(1, n + 1):
    # Print spaces before the stars
    print(" " * (n - i), end="")
    # Print the stars for the current row
    print("*" * (2 * i - 1))
