# Challenge 10: Smallest Number

# Find the Smallest number in an array.

# Example:
# [4, 10, 2, 8, 15, 3]

# Output:
# 2

number = [4, 10, 2, 8, 15, 3]
min = number[0]

for i in range(1, len(number)):
  if number[i] < min:
    min = number[i]

print(min)