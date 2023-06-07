//  equivalent to print
alert('Hello World')
console.log('Hello from the console')
// console.error("error")
// console.warn('warn')
// console.table(["table", 4, "potato"])
// console.info('info')

// equivalent to input
let color = prompt('Enter your favorite color')

color = 'red'

alert("You entered " + color)

// var
// let - used for mutable data
// const - used for non-unmutable data
let animal = 'dog'

// String
'hello'
"hello"
// `hello`

// Number
8
5.4

// Boolean
true
false

// Array - effectively a list
[1, 2, 3]

// Object - effectively a dict
let person = {
    'firstname': 'joe',
    'lastname': 'fred'
}

let person2 = {
    firstname: 'Carly',
    lastname: 'Steveneson'
}

// Both are equivalent
alert(person['firstname'])
alert(person2.firstname)

let petName
// undefined   
undefined

//  null - equivalent to None
null


/*
temp = 78 
if temp > 75:
    print('its warm')
*/

//  Conditionals
let temp = 78
if (temp > 75){
    console.log(`${temp} is warm`)
}
else if(temp< 70){
    console.log("It is chilly")
}
else{
    console.log("Perfect")
}

// line templates
`${temp}`


