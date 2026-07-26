# Challenge 09: Multiplication Table

# Print the multiplication table for a given number.

# Example:
# Input: 5

# Output:
# 5 x 1 = 5
# ...
# 5 x 10 = 50

total = 0
number = int(input("Input a Number : "))

for x in range(1, number + 1):
  if x <= number:
    total = number * x
    print(total)