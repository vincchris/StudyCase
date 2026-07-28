/*
Challenge 12: Largest of Two Numbers

Find the larger value between two numbers.

Example:
Input:
15
7

Output:
15
*/

let number = [15, 20, 1]
let max = number[0]

for (let i = 1; i < number.length; i++) {
  if (number[i] > max) {
    max = number[i]
  }
}

console.log(max)