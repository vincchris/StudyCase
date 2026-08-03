# Challenge 19: Sum of Odd Numbers

# Calculate the sum of all
# odd numbers from 1 to N.

# Example:
# Input: 10

# Output:
# 25

number = int(input("Enter a Number : "))
total = 0

for i in range(1, number + 1):
  if (i % 2):
    total += i

print(total)