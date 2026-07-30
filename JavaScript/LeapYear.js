/*
Challenge 14: Leap Year

Determine whether a given year
is a leap year.

Example:
Input: 2024

Output:
Leap Year
*/

let number = 2023

if (number % 400 === 0) {
  console.log("Leap Year")
} else if (number % 100 === 0) {
  console.log("Not Leap Year")
} else if (number % 4 === 0) {
  console.log("Leap Year")
} else {
  console.log("Not Leap Year")
}