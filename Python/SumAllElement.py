# Challenge 24: Sum All Elements

# Calculate the total sum
# of every element in an array.

# Example:
# [2,4,6]

# Output:
# 12

# Step One
# number = [2, 4, 6]
# print(sum(number))

# Step two
number = [2, 4, 6]
count = 0

for i in range(len(number)):
  count += number[i]

print(count)