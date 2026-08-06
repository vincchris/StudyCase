# Challenge 22: Count Even Numbers

# Count how many even
# numbers exist in an array.

# Example:
# [1,2,3,4,5,6]

# Output:
# 3

number = [1, 2, 3, 4, 5, 6]
count = 0
n = len(number)

for i in range(n):
  if number[i] % 2 == 0:
    count += 1

print(count)