# Challenge 27: Count Negative Numbers

# Count how many negative numbers
# exist in an array.

# Example:
# [2, -4, 5, -1, 8]

# Output:
# 2

numbers = [2, -4, 5, -1, 8]
negative = 0

for i in range(len(numbers)):
  if numbers[i] < 0:
    negative += 1

print(negative)