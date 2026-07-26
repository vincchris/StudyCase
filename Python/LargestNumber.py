# Challenge 08: Largest Number

# Find the largest number in an array.

# Example:
# [4, 10, 2, 8, 15, 3]

# Output:
# 15

number = [4, 10, 2, 8, 15, 3]
max = number[0]
n = len(number)

for i in range(1, n):
  if number[i] > max:
    max = number[i]

print(max)