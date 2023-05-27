let userGuess = document.querySelector("#user-guess")
let guessBtn = document.querySelector("#guess-btn")
let results = document.querySelector("#results")

guessBtn.style.backgroundColor = "lightblue"


guessBtn.addEventListener("click", function() {
    const guess = userGuess.valueAsNumber

    const randomNumber = Math.floor(Math.random() * 10)

    if(guess == randomNumber){
        // correct
        results.textContent = "You guessed correctly!!!!"
    }
    else if(guess > randomNumber){
        // guessed too high
        results.textContent = "Too high! Try again."
    }
    else {
        // guessed too low
        results.textContent = "Too low, try again."
    }
})

// function guessTheNumber() {
//     const guess = userGuess.valueAsNumber

//     const randomNumber = Math.floor(Math.random() * 10)

//     if(guess == randomNumber){
//         // correct
//         results.textContent = "You guessed correctly!!!!"
//     }
//     else if(guess > randomNumber){
//         // guessed too high
//         results.textContent = "Too high! Try again."
//     }
//     else {
//         // guessed too low
//         results.textContent = "Too low, try again."
//     }
// }

// guessBtn.addEventListener("click", guessTheNumber)