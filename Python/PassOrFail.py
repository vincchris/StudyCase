# Challenge 03: Pass or Fail

# Determine whether a student passes or fails based on the score.

# Rules:
# - Score >= 75 → Pass
# - Otherwise → Fail

# Example:
# Score = 80

# Output:
# Pass

score = int(input("Input Number : "))

if score >= 75:
  print("Pass")
else:
  print("Fail")