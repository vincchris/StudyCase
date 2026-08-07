/*
Challenge 23: Count Odd Numbers

Count how many odd
numbers exist in an array.

Example:
[1,2,3,4,5,6]

Output:
3
*/

let number = [1, 2, 3, 4, 5, 6]
let count = 0

for (let i = 0; i <number.length; i++) {
  if (number[i] % 2 !== 0) {
    count++
  }
}

console.log(count)