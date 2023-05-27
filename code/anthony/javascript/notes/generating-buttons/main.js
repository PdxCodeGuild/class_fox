let addBtn = document.querySelector("#add-btn")
let removeBtn = document.querySelector("#remove-btn")
let items = document.querySelector("#items")

let count = 0

addBtn.addEventListener("click", function(){
    let newLi = document.createElement("li")
    newLi.textContent = count
    items.appendChild(newLi)
    count++
})

removeBtn.addEventListener("click", function(){
    items.removeChild(items.firstChild)
})

