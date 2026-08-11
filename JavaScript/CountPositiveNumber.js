/*
Challenge 27: Count Positive Numbers

Count how many positive numbers
exist in an array.

Example:
[2, -4, 5, -1, 8]

Output:
3
*/

let number = [2, -4, 5, -1, 8]
let positive = 0

for (let i = 0; i < number.length; i++) {
  if (number[i] > 0) {
    positive++
  }
}

console.log(positive)