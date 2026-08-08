/*
Challenge 24: Sum All Elements

Calculate the total sum
of every element in an array.

Example:
[2,4,6]

Output:
12
*/

let number = [2, 4, 6]
count = 0

for (let i = 0; i < number.length; i++) {
  count += number[i]
}

console.log(count)