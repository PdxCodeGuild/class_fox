// exercise 1

// let name = prompt("What is your name?")
// let age = prompt("What is you age?")

// alert("Hello " + name + " you are " + age + " years old.")

// exercise 2

// let number1 = parseInt(prompt("Enter a number: "))
// let number2 = parseInt(prompt("Enter another number: "))
// let addition = number1 + number2
// let subtraction = number1 - number2
// let multiplier = number1 * number2
// let division = number1 / number2
// let mod = number1 % number2


// alert(`${number1} + ${number2} = ${addition} \n
//     ${number1} - ${number2} = ${subtraction} \n
//     ${number1} * ${number2} = ${multiplier} \n
//     ${number1} / ${number2} = ${division} \n
//     ${number1} % ${number2} = ${mod}`
//     )

// exercise 3

// let f = parseInt(prompt("Enter a temperature in Fahrenheit: "))
// let c = (f - 32 * .5556)

// alert(`${f} degrees Fahrenheit is ${c} degrees Celsius`)

// exercise 4 

randomNumber = Math.floor(1 + Math.random() * 100)
let usersNumber = parseInt(prompt("Enter a number between 1 and 100: "))

if ( randomNumber == usersNumber) {
    alert("Correct")
}

else if (randomNumber > usersNumber) {
    alert("Too low!")
}

else {
    alert("Too high!")
}



