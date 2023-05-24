// equivalent to print
// alert("Hello World!")
// console.log("Hello from the console!")
// console.error("error")
// console.warn("warning")
// console.table(["table", "potato", 4])
// console.info(["info", "potato", 4])

// equivalent to input
// let color = prompt("Enter your favorite color")

color = "red"

// alert("You entered " + color)

// var
// let - used for mutable data
// const - used for non-mutable data
let animal = "dog"

// String
"hello";
'hello';
`hello`;

// Number
8
5.4

// Boolean
true
false

// Array - effectively a list
[1, 2, 3]

// Object - effectively a dictionary
let person = {
    "firstName": "Joe",
    "lastName": "Fred"
}

let person2 = {
    firstName: "Carly",
    lastName: "Stevenson",
    favFoods: ["mushrooms", "something else"],
    address: {
        street: "1234 1st st",
        zip: "12345"
    }
}

// alert(person["firstName"])
// alert(person.lastName)
// alert(person2.firstName)

let petName
// console.log(petName)

// undefined
undefined

// null - equivalent to None
null



/*
temp = 78
if temp > 75:
    print(f"{temp} is warm")
*/

let temp = 78
if (temp > 75){
    console.log(`${temp} is warm`)
}
else if (temp < 70){
    console.log("It is chilly")
}
else{
    console.log("Perfect!")
}

console.log('This is\
a multi\
line string')