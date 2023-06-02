let userGuess = document.querySelector("#user-guess")
let guessBtn = document.querySelector("#guess-btn")
let results = document.querySelector("#results")

guessBtn.addEventListener("click", function() {
    const guess = user.Guess.valueAsNumber

    const randomNumber = Math.floor(Math.random() * 10)

    if(guess == randomNumber){
        results.textContent = "You guessed correct"
    }
    else if (guess > randomNumber){
        results.textContent = "You guessed too high"
    }
    else{
        results.textContent = "You guessed too low"
    }
})