/*
Challenge 30: Find Numbers Less Than 10

Print all numbers smaller than 10.

Example:
[4, 12, 7, 20, 3]

Output:
4
7
3
*/

let numbers = [4, 12, 7, 20, 3]

for (let i = 0; i < numbers.length; i++) {
  if (numbers[i] < 10) {
    console.log(numbers[i])
  }
}