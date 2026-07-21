# Challenge 05: Shopping Discount

# Apply a 10% discount if the total purchase exceeds 100000.

# Example:
# Total = 150000

# Output:
# 135000

totalPurchase = int(input("Input a Number : "))

if totalPurchase > 100000:
  totalPurchase -= totalPurchase / 10

print(int(totalPurchase))