# Challenge 25: Reverse an Array

# Reverse the array
# without using reverse().

# Example:
# [1,2,3]

# Output:
# [3,2,1]

number = [1, 2, 3]
reserved_number = []
number_length = len(number)

for i in range(number_length - 1, -1, -1):
  reserved_number.append(number[i])
print(reserved_number)