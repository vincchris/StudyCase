# Challenge 30: Find Numbers Less Than 10

# Print all numbers smaller than 10.

# Example:
# [4, 12, 7, 20, 3]

# Output:
# 4
# 7
# 3

number = [4, 12, 7, 20, 3]

for i in range(len(number)):
  if number[i] < 10:
    print(number[i])