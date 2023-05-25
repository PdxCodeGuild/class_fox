


// def name_of_function(parameters):

function nameOfFunction(parameters){
    // body
}


const add = function(num1, num2){
    let sum = num1 + num2
    return sum
}

let result = add(2, 4)
console.log(result)
console.log(add(3, 5))
console.log(add(7, 2))
console.log(add("apple", "banana"))



function greeting(name){
    console.log(`Hello ${name}`)
}

greeting("Bruce")



const subtract = function(num1, num2){
    return num1 - num2
}

// function prettyPrint(func, arg1, arg2){

//     let result = func(arg1, arg2)

//     console.log(`The result of ${arg1} and ${arg2} is ${result}`)
// }

// prettyPrint(subtract, 12, 6)
// prettyPrint(add, 512, 256)


const randomNumber = (startingNumber = 0, endingNumber = 10) => {
    number = Math.floor(Math.random() * (endingNumber - startingNumber + 1) + startingNumber)
    return number
}

console.log(randomNumber(50, 60))



let grades = [88, 89, 76, 100, 1]
grades.sort(function (){

})