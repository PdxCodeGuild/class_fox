let dealerHand = document.querySelector("#dealer-hand")
let dealerScore = document.querySelector("#dealer-score")
let playerHand = document.querySelector("#player-hand")
let playerScore = document.querySelector("#player-score")
let newGameBtn = document.querySelector("#new-game-btn")
let hitBtn = document.querySelector("#hit-btn")
let stayBtn = document.querySelector("#stay-btn")
let results = document.querySelector("#results")


// global variables
let deckId = ""
let dealerCards = []
let playerCards = []

// Get a new deck id from API
async function newDeck(){
    let response = await axios.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=6")
    deckId = response.data.deck_id
}

// get new deck id as soon as page loads
newDeck()


// deal cards to player dealer
async function dealCards(){
    let response = await axios.get(`https://deckofcardsapi.com/api/deck/${deckId}/draw/?count=4`)
    
    for(let i in response.data.cards){
        if(i % 2 == 0){
            playerCards.push(response.data.cards[i])
        } else {
            dealerCards.push(response.data.cards[i])
        }
    }
    renderCards(playerCards, playerHand, playerScore)
    renderCards(dealerCards, dealerHand, dealerScore)
}


// render cards
function renderCards(cards, container, score){
    container.innerHTML = ""
    for(let card of cards){
        let img = document.createElement("img")
        img.src = card.image
        img.style.height = "100px"
        container.appendChild(img)
    }

    let total = calculateScore(cards)
    score.textContent = `Score: ${total}`
    if(total >= 21){
        hitBtn.disabled = true
    }
}

async function drawSingleCard(){
    let response = await axios.get(`https://deckofcardsapi.com/api/deck/${deckId}/draw/?count=1`)
    return response.data.cards[0]
}

function calculateScore(cards){
    let total = 0
    for(let card of cards){
        if(card.value === "ACE"){
            total += 1
        } else if (Number(card.value)){
            total += Number(card.value)
        } else {
            total += 10
        }
    }
    return total
}

newGameBtn.addEventListener("click", function() {
    dealerCards = []
    playerCards = []
    hitBtn.disabled = false
    results.textContent = ""
    dealCards()
})

hitBtn.addEventListener("click", async function(){
    let card = await drawSingleCard()
    playerCards.push(card)
    renderCards(playerCards, playerHand, playerScore)
})

stayBtn.addEventListener("click", async function(){
    hitBtn.disabled = true
    let player_score = calculateScore(playerCards)
    let dealer_score = calculateScore(dealerCards)
    
    if(player_score > 21) {
        results.textContent = "Dealer wins, you busted"
        return
    }
    
    while(dealer_score < 17){
        if(dealer_score > player_score){
            break
        }
        let card = await drawSingleCard()
        dealerCards.push(card)
        renderCards(dealerCards, dealerHand, dealerScore)
        dealer_score = calculateScore(dealerCards)
    }


    if(player_score < dealer_score){
        results.textContent = "Dealer wins!!"
    }
    else if(player_score === dealer_score){
        results.textContent = "Dealer wins!!!"
    }
    else{
        results.textContent = "Player wins!"
    }
})