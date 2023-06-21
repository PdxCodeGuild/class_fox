let inputString = document.querySelector('#input-string')
let rotation = document.querySelector('#rotate')
let button = document.querySelector('#button')
let output = document.querySelector("#output")

addEventListener('click', function(){
    characters = 'abcdefghijklmnopqrstuvwxyz'
    let outputString = ""
    
    for(let char of inputString.value){
        if(characters.includes(char)){
            let i = characters.indexOf(char)
    
            i = (i + rotation.valueAsNumber) % characters.length
            
            outputString += characters[i]
    
        } else{
            outputString += char
        }
    }
        output.textContent = outputString
    })