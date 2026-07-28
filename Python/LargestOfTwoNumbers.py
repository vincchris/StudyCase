# Challenge 12: Largest of Two Numbers

# Find the larger value between two numbers.

# Example:
# Input:
# 15
# 7

# Output:
# 15

number = [15, 7, 100]
max = number[0]
n = len(number)

for i in range(1, n):
  if number[i] > max:
    max = number[i]

print(max)