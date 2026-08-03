/*
Challenge 18: Sum of Even Numbers

Calculate the sum of all
even numbers from 1 to N.

Example:
Input: 10

Output:
30
*/

let number = 10
let total = 0

for (let i = 1; i <= number; i++) {
  if (i % 2 === 0) {
    total += i
  }
}

console.log(total)
