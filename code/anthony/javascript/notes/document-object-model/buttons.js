let body = document.querySelector("body")

for(let i = 0; i < 10; i++){
    // Create button
    let newButton = document.createElement("button")
    
    // edit button
    newButton.textContent = i + 1
    
    // add button to body
    body.appendChild(newButton)
}