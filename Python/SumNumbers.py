# Challenge 08: Sum Numbers

# Calculate the sum of all numbers from 1 to 5.

# Output:
# 15

total = 0
number = int(input("User Input Number: "))

for i in range(number):
  total += i

print(total)