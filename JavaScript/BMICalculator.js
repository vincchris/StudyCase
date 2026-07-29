/*
Challenge 13: BMI Category

Determine the BMI category
based on the given BMI value.

Example:
BMI: 22

Output:
Normal
*/

let number = 20

if (number <= 18) {
  console.log("UnderWeight")
}

else if (number <= 20) {
  console.log("normal")
}

else if (number <= 25) {
  console.log("OverWeight")
}

else {
  console.log("Obesity")
}
