/*
Challenge 19: Sum of Odd Numbers

Calculate the sum of all
odd numbers from 1 to N.

Example:
Input: 10

Output:
25
*/

let number = 10
let total = 0

for (let i = 0; i <= number; i++) {
  if (i % 2) {
    total += i
  }
}

console.log(total)