
// while loops

// while (condition){
//      body
// }

// while condition:
//      body

// break and continue work the same as in python

// let counter = 0
// while(counter < 10){
//     counter++   // counter += 1 or counter = counter + 1
//     console.log(`${counter} Hello`)
// }


// for loops

// for(initial counter; condition; increment){
//      body
//}

// for(let i = 0; i < 10; i++){
//     console.log(`${i} Goodbye`)
// }

let names = ["Harry", "Ron", "Hermione"]
// for(let i = 0; i < 3; i++){
//     console.log(names[i])
// }

// for name in names:

// let variable in variables will loop over indexes
// for(let i in names){
//     console.log(i)
// }

// let variable of variables will loop over elements
// for(let name of names){
//     console.log(name)
// }


let person = {
    firstName: "Fred",
    lastName: "Wesley",
    house: "Gryffindor"
}

for(let key in person){
    console.log(key)
}

for(let value of Object.values(person)){
    console.log(value)
}


// Array.length
// Object.values
// Number.isInteger("4")



names = ["Harry", "Ron", "Hermione"]
console.log(names[80])


function printName(character){
    console.log(character)
}

names.forEach(printName)