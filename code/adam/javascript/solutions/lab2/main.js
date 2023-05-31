let firstHand = document.querySelector("#firstCard")
let secondHand = document.querySelector("#secondCard")
let thirdHand = document.querySelector("#thirdCard")
let confirmBtn = document.querySelector("#confirmBtn")
let phrase = document.querySelector('#phrase')
let totalScore = document.querySelector('#totalScore')


let blackjack = {A: 1,
J: 10,
Q: 10,
K: 10,
2: 2,
3: 3,
4: 4,
5: 5,
6: 6,
7: 7,
8: 8,
9: 9,
10: 10
}


confirmBtn.addEventListener("click", function(){
    
    let firstCard = firstHand.value
    let secondCard = secondHand.value
    let thirdCard = thirdHand.value
    
    console.log(firstCard, firstCard in blackjack)
    console.log(secondCard, secondCard in blackjack)
    console.log(thirdCard, thirdCard in blackjack)

    if(firstCard in blackjack && secondCard in blackjack && thirdCard in blackjack){
    
        let total = blackjack[firstCard] + blackjack[secondCard] + blackjack[thirdCard]
        console.log(total)
        if(total < 17){
            totalScore.textContent = `Your total is - ${total}`
            phrase.textContent = "Hit!"
    }
        else if(total >= 17 && total < 21){
            totalScore.textContent = `Your total is - ${total}`
            
            phrase.textContent = "Stay!"
    }
        else if(total == 21){
            totalScore.textContent = `Your total is - ${total}`
            
            phrase.textContent = "Blackjack!"
    }
        else{
            totalScore.textContent = `Your total is - ${total}`
            
            phrase.textContent = "Busted!"
        }}

    else{
        phrase.textContent = "Enter a valid card"
    }
    
})

  
