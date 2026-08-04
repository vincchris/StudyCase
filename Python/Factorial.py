# Challenge 20: Factorial

# Calculate the factorial
# of a given number.

# Example:
# Input: 5

# Output:
# 120

number = int(input("Enter a Number : "))
total = 1

for i in range(1, number + 1):
  total = total * i

print(total)