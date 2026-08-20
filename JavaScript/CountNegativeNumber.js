// Challenge 29: Count Negative Numbers
// Count how many negative numbers
// exist in an array.

// Example:
// [2, -4, 5, -1, 8]

// Output:
// 2

let numbers = [2, -4, 5, -1, 8]
let negative = 0

for (let i = 0; i < numbers.length; i++) {
  if (numbers[i] < 0) {
    negative++
  }
}

console.log(negative)