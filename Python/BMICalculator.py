# Challenge 13: BMI Category

# Determine the BMI category
# based on the given BMI value.

# Example:
# BMI: 22

# Output:
# Normal

number = int(input("Input a Number : "))

if number < 18.5:
  print("Underweight")
elif number < 25:
  print("normal")
elif number < 30:
  print("OverWeight")
else:
  print("Obesity")