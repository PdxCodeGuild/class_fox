

//  while loop:
// while (condition){
//      body
// } 

//  break and continue work the same as in python

// let counter = 0
// while(counter < 10){
//     counter++
//     console.log(`${counter} Hello`)
// }


// for loops:

// for(let i = 0; i < 10; i++){
//     console.log(`${i} Goodbye`)
// }

// let names = ["harry", "ron", "hermione"]
// for(let i = 0; index < 3; i++){
//     console.log(names[i])
// }

// "of" loops over elements in array
// for(let name of names){
//     console.log(name)
// }

// "in" loops over indices in array
// for(let name in names){
//     console.log(name)
// }

let person = {
    firstname: "fred",
    lastname: "weasley",
    house: "Gryffindor"
}

for(let key in person){
    console.log(key)
}

for(let value of Object.values(person)){
    console.log(value)
}



// Array.length
// Objects.values
// Number.isInteger("2")


// for each loop
names = ["harry", "hermione", "ron"]

function printName(name){
    console.log(name)
}
names.forEach(printName)