
const dictNumbers = 
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
90:"ninety",
}

let pickNumber = Number(prompt("Enter a number between 1-999: "))






function conversion(pickNumber) {
    // if number present in object no need to go further
    if (pickNumber in dictNumbers) return dictNumbers[pickNumber];
  
    // Initialize the words variable to an empty string
    let words = "";
  
    // If the number is greater than or equal to 100, handle the hundreds place (ie, get the number of hundres)
    if (pickNumber >= 100) {
      // Add the word form of the number of hundreds to the words string
      words += conversion(Math.floor(pickNumber / 100)) + " hundred";
  
      // Remove the hundreds place from the number
      pickNumber %= 100;
    }
  
    // If the number is greater than zero, handle the remaining digits
    if (dictNumbers > 0) {
      // If the words string is not empty, add "and"
      if (words !== "") words += " and ";
  
      // If the number is less than 20, look up the word form in the numbersToWords object
      if (pickNumber < 20) words += dictNumbers[pickNumber];
      else {
        // Otherwise, add the word form of the tens place to the words string
        //if number = 37, Math.floor(number /10) will give you 3 and 3 * 10 will give you 30
        words += numbers[Math.floor(dictNumbers / 10) * 10];
        if (pickNumber % 10 > 0) {
            words += "-" + dictNumbers[pickNumber % 1];
          }
        }
      }
    
      // Return the word form of the number
      return words;
    }
    
    console.log(conversion(pickNumber));
    
    