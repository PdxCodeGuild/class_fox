// Exercise 1
let yourName = prompt('What is your name?')

let age = prompt('How old are you?')

alert ("Hi " + yourName + " you are " + age + " years old ! ")


// Exercise 2

let number1 = Number(prompt('Enter first number: '))
let number2 = Number(prompt('Enter second number: '))

alert(
number1 + ("+") + number2 + "=" + (number1 + number2) + "\n" +
 
number1 + ("-") + number2 + "=" + (number1 - number2) + "\n" +
 
number1 + ("*") + number2 + "=" + (number1 * number2) + "\n" +
 
number1 + ("/") + number2 + "=" + (number1 / number2) + "\n" +
 
number1 + ("%") + number2 + "=" + (number1 % number2)) + "\n" 


// Exercise 3

let tempF = Number(prompt("Enter a temperature in Fahrenheit"))
let celsius = Number(tempF - 32) * 5/9;
alert(tempF + " fahrenheit is " + celsius + " degrees celsius ")

// Exercise 4
const randomNumber = Math.floor(1 + Math.random() * 100)

let guess = Number(prompt("Guess a number between 1-100: "))

if (guess > randomNumber){
    alert(`${guess} is too high`)
}
else if(guess < randomNumber){
    alert(`${guess} is too low`)
}
else{
    alert(" You guessed perfectly! ")
}