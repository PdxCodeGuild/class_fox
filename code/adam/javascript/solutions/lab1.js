

const numbers = 
{0:"",
1:"one", 
2:"two", 
3:"three", 
4:"four",
5:"five", 
6:"six", 
7:"seven", 
8:"eight", 
9:"nine", 
10:"ten",
11:"eleven", 
12:"twelve", 
13:"thirteen", 
14:"fourteen", 
15:"fifteen", 
16:"sixteen",
17:"seventeen",
18:"eighteen",
19:"nineteen",
20:"twenty",
30:"thirty",
40:"fourty",
50:"fifty",
60:"sixty",
70:"seventy",
80:"eighty",
90:"ninety"
}

// allows user to pick their own number to change it to phrase form
let pickNumber = Number(prompt("Enter a number between 1-999: "))

function conversion(pickNumber){
    if(pickNumber in numbers) return numbers[pickNumber];

    let words = '';


    //  hundreds place
    if(pickNumber >= 100){
        words = words + conversion(Math.floor(pickNumber / 100)) + " hundred";
        pickNumber = pickNumber % 100;
    }

    // if number is greater than zero add the "and" to the phrase
    if(pickNumber > 0){
        if(words !== "") words += " and ";
        

        if(pickNumber < 20) words += numbers[pickNumber];
        
        //  tens place
        else{
            words += numbers[Math.floor(pickNumber / 10) * 10];
            
            //  ones place
            if (pickNumber % 10 > 0){
                // concat words + the numbers from dict and add "-" between the tens and ones place
                words += "-" + numbers[pickNumber % 10]
            }
        }
    }

    return words;
}
console.log(conversion(pickNumber))
