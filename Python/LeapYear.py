# Challenge 14: Leap Year

# Determine whether a given year
# is a leap year.

# Example:
# Input: 2024

# Output:
# Leap Year

number = int(input("Enter a Number : "))

if number % 400 == 0:
  print("Leap Year")
elif number % 100 == 0:
  print("Not Leap Year")
elif number % 4 == 0:
  print("Leap Year")
else:
  print("Not Leap Year")
