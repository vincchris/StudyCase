# Challenge 27: Count Positive Numbers

# Count how many positive numbers
# exist in an array.

# Example:
# [2, -4, 5, -1, 8]

# Output:
# 3

number = [2, -4, 5, -1, 8]
positive = 0

for i in range(len(number)):
  if number[i] > 0:
    positive += 1

print(positive)