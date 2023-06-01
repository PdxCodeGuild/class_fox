let inputString = document.querySelector("#input-string")
let rotationAmount = document.querySelector("#rotation-amount")
let button = document.querySelector("#button")
let output = document.querySelector("#output")
// let output = document.getElementById("output")

button.addEventListener("click", function(){
    let characters = "abcdefghijklmnopqrstuvwxyz"
    let outputString = ""

    for(let char of inputString.value){
        if(characters.includes(char)){
            let i = characters.indexOf(char)

            i = (i + rotationAmount.valueAsNumber) % characters.length

            outputString += characters[i]
        } else {
            outputString += char
        }
    }

    output.textContent = outputString
})