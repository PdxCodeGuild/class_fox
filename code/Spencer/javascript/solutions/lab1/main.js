
// BLACKJACK!

// let blackjack = {
//     "A": 1,
//     "2": 2,
//     "3": 3,
//     "4": 4,
//     "5": 5,
//     "6": 6,
//     "7": 7,
//     "8": 8,
//     "9": 9,
//     "10": 10,
//     "J": 10,
//     "Q": 10,
//     "K": 10,
// }


// let first_card = prompt("Enter your first card: ")  
// let second_card = prompt("Enter your second card: ") 
// let third_card = prompt("Enter your third card: ") 

// if (`${first_card} in blackjack && ${second_card} in blackjack && ${third_card} in blackjack`){
    
//     let result = blackjack[first_card] + 
//         blackjack[second_card] + blackjack[third_card]

  
    
//     if (result < 17){
//         alert("Hit!")}
    
//     else if (result >= 17 && result < 21){
//         alert("Stay")}
    
//     else if (result == 21){
//         alert("Blackjack!")}
   
//     else{
//         alert("Busted")}

//     alert(`Total: ${result}`)}
// else{
//     alert("Invalid input")}







// PICK 6!!!!!!!!

// function pick6(startingNumber=0, endingNumber=99){
//    let ticket = []
//     for (let x = 0; x < 6; x++){
//         ticket.push(Math.floor(Math.random(1, 99)))}

//     return ticket
// }
// function calculate_winnings(matches){
//     if (matches == 1){
//         return 4}
//     else if (matches == 2){
//         return 7}
//     else if (matches == 3){
//         return 100}
//     else if (matches == 4){
//         return 50_000}
//     else if (matches == 5){
//         return 1_000_000}
//     else if (matches == 6){
//         return 25_000_000}

//     return 0}


// function get_number_of_matches(ticket, winning_ticket){
//     let matches = 0
//     for (let x = 0; x < 6; x++){
//         if (ticket[x] == winning_ticket[x]){
//             let matches = matches + 1}

//     return matches}}

// let winning_ticket = pick6()

// let balance = 0
// for (let x = 0; x < 100,000; x++){

//     let ticket = pick6()
//     balance = balance - 2

//     let matches = get_number_of_matches(ticket, winning_ticket)
//     balance = balance + calculate_winnings(matches)}

// alert(`You have earned ${balance}`)
// let roi = balance / 200_000
// alert(`Your ROI is: ${roi * 100}%`)








// CREDIT CARD VALIDATOR

function credit_card_validator(){
let starting_string = prompt("Enter card number: ")  

    
    let credit_card_number = starting_string.split("")
    
    for (let x = 0; x < credit_card_number.length; x++){
        credit_card_number[x] = parseInt(credit_card_number[x])}

    let check_digit = credit_card_number.pop()

    credit_card_number.reverse()

    for (let x = 0; x < credit_card_number.length; x++){
        if (x % 2 == 0){
            credit_card_number[x] = credit_card_number[x] * 2}

        if (credit_card_number[x] > 9){
            credit_card_number[x] = credit_card_number[x] - 9}}
    let total = 0
    for (x in credit_card_number){
        total = x + total
    }


    let second_digit = total 
    second_digit = second_digit % 10

    if (second_digit == check_digit){
        return true}
    else{
        return false}}


let result = credit_card_validator()
alert(result)