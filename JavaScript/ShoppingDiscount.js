/*
Challenge 05: Shopping Discount

Apply a 10% discount if the total purchase exceeds 100000.

Example:
Total = 150000

Output:
135000
*/

let currentTotal = 150000

if (currentTotal >= 100000) {
  currentTotal = currentTotal - (currentTotal / 10)
}

console.log(currentTotal)