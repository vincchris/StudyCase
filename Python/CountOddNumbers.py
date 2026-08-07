# Challenge 23: Count Odd Numbers

# Count how many odd
# numbers exist in an array.

# Example:
# [1,2,3,4,5,6]

# Output:
# 3

number = [1, 2, 3, 4, 5, 6]
count = 0

for i in range(len(number)):
  if (number[i] % 2 != 0):
    count += 1

print(count)