let userGuess = document.querySelector('#user-guess')
let guessBtn = document.querySelector('#guess-btn')
let results = document.querySelector('#results')

guessBtn.textContent = "Guess number"

guessBtn.style.backgroundColor = "lightblue"

guessBtn.addEventListener("click", function(){
    const guess = userGuess.valueAsNumber

    const randomNumber = Math.floor(Math.random() * 10)

    if(guess == randomNumber){
        results.textContent = 'Correct, you guessed correctly!'
    }
    else if(guess > randomNumber){
        results.textContent = 'Your guess is too high'
    }else{
        guess < randomNumber
        results.textContent = 'Your guess is too low'
    }
})