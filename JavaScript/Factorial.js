/*
Challenge 20: Factorial

Calculate the factorial
of a given number.

Example:
Input: 5

Output:
120
*/

let number = 5
let total = 1

for (let i = 1; i <= number; i++) {
  total = total * i
}

console.log(total)