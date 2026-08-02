# Challenge 17: Sum from 1 to N

# Calculate the sum of all
# numbers from 1 to N.

# Example:
# Input: 5

# Output:
# 15

number = int(input("Input a Number : "))
total = 0

for i in range(0, number + 1):
  total += i

print(total)