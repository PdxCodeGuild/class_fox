


// def name_of_function(parameters)

function nameOfFunction(parameters){
    // body
}


function add(num1, num2){
    let sum = num1 + num2
    return sum
}

let result = add(6, 2)
console.log(result)
console.log(add(2, 10))
console.log(add(100, 5))
console.log(add("apple", "banana"))



function greeting(name){
    console.log(`Hello ${name}`)
}

greeting("Adam")



const subtract = function(num1, num2){
    return num1 - num2
}

// function prettyPrint(func, arg1, arg2){
//     let result = func(arg1, arg2)

//     console.log(`The result of ${arg1} - ${arg2} is ${result}`)
// }

// prettyPrint(subtract, 12, 6)



const randomNumber = (startingNumber, endingNumber) => {
   number = Math.floor(Math.random() * (endingNumber - startingNumber + 1) + startingNumber)
   return number
}
console.log(randomNumber(30, 200))


let grades = [88, 89, 76, 100, 1]
grades.sort(function (){

})