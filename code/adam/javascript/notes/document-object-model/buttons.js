let body = document.querySelector('body')

for(let i = 0; i < 10; i++){
    //  Create button
    let newButton = document.createElement("button")
    
    //  add button to page
    body.appendChild(newButton)
    //  give button
    newButton.textContent = i + 1
}