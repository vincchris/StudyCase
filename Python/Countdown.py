# Challenge 16: Countdown

# Print all numbers from
# N down to 1.

# Example:
# Input: 5

# Output:
# 5
# 4
# 3
# 2
# 1

number = int(input("Input a Number : "))

for i in range(number, 0, -1):
  print(i)