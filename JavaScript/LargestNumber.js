/*
Challenge 09: Largest Number

Find the largest number in an array.

Example:
[4, 10, 2, 8, 15, 3]

Output:
15
*/

let number = [4, 10, 2, 8, 15, 3]
let max = number[0]

for (let i = 1; i < number.length; i++) {
  if (number[i] > max) {
    max = number[i]
  }
}

console.log(max)
