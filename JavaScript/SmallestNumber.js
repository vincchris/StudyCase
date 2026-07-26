/*
Challenge 10: Smallest Number

Find the Smallest number in an array.

Example:
[4, 10, 2, 8, 15, 3]

Output:
2
*/

let number = [4, 10, 8, 15, 3]
let max = number[0]

for (let i = 1; i < number.length; i++) {
  if (number[i] < max) {
    max = number[i]
  }
}

console.log(max)