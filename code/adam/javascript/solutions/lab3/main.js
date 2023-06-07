// let phrase = document.querySelector('#phrase')
let roiPhrase = document.querySelector('#roiPhrase')
const outputDiv = document.getElementById('output');



// Generate a random integer between 0 and 99
function getRandomInt(min=0, max=99) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Generate an array of 6 numbers as the winning numbers
function generatePicks() {
    const picks = [];
    while (picks.length < 6) {
        const pick = getRandomInt(1, 99);
        if (!picks.includes(pick)) {
            picks.push(pick);
        }
    }
    return picks;
}

//  return the number of matching elements
function comparePicks(picks1, picks2) {
    let count = 0;
    for (let i = 0; i < picks1.length; i++) {
        if (picks2.includes(picks1[i])) {
            count++;
        }
    }
    return count;
}

// Play the pick6 game 
function playPick6(numRounds) {
    let totalWinnings = 0;
    for (let i = 0; i < numRounds; i++) {
        const picks = generatePicks();
        const winningPicks = generatePicks();
        const numMatches = comparePicks(picks, winningPicks);
        let winnings = 0;
        if (numMatches === 0) {
            winnings = 0;
        } else if (numMatches === 1) {
            winnings = 4;
        } else if (numMatches === 2) {
            winnings = 7;
        } else if (numMatches === 3) {
            winnings = 100;
        } else if (numMatches === 4) {
            winnings = 50000;
        } else if (numMatches === 5) {
            winnings = 1000000;
        } else if (numMatches === 6) {
            winnings = 25000000;
        }
        totalWinnings += winnings;
        const roundOutput = `Picks: ${picks}<br>Winning picks: ${winningPicks}<br>Matches: ${numMatches}<br>Winnings: $${winnings}<br><br>`;
        outputDiv.innerHTML += roundOutput;}}
        
        
        