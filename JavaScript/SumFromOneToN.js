/*
Challenge 17: Sum from 1 to N

Calculate the sum of all
numbers from 1 to N.

Example:
Input: 5

Output:
15
*/

let number = 5
let total = 0

for (let i = 1; i <= number; i++) {
  total += i
  console.log(total)
}