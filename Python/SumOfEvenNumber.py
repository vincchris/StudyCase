# Challenge 18: Sum of Even Numbers

# Calculate the sum of all
# even numbers from 1 to N.

# Example:
# Input: 10

# Output:
# 30

number = int(input("Enter a Number : "))
total = 0

for i in range(1, number + 1):
  if i % 2 == 0:
    total += i

print(total)