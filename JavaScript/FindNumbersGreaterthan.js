/*
Challenge 25: Find Numbers Greater Than 50

Print all values greater
than 50.

Example:
[12,60,45,90]

Output:
60
90
*/

let number = [12, 60, 45, 90]

for (let i = 0; i < number.length; i++) {
  if (number[i] > 50) {
    console.log(number[i])
  }
}
