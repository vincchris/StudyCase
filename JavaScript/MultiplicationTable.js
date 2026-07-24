/*
Challenge: Multiplication Table

Print the multiplication table for a given number.

Example:
Input: 5

Output:
5 x 1 = 5
...
5 x 10 = 50
*/

let total = 0
let number = 5

for (let i = 1; i <= number; i++) {
  total = number * i
  console.log(total)
}
