# Challenge 25: Find Numbers Greater Than 50

# Print all values greater
# than 50.

# Example:
# [12,60,45,90]

# Output:
# 60
# 90

number = [12, 60, 45, 90]

for i in range(len(number)):
  if number[i] > 50:
    print(number[i])