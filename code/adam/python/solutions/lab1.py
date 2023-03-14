"""
Lab 1: Numbers to phrases
Date: Mar 10th, 2023
"""




numbers = {0:"",
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
100:"hundred",
200:" hundred", 
300:" hundred", 
400:"hundred",
500:"hundred",
600:"hundred",
700:"hundred",
800:" hundred",
900:" hundred"}

num = int(input("Enter a number: "))
if num <= 999:
    if num in numbers:
        conversion = numbers.get(num)
        print(conversion)
    else:
        hundred_digit = num//100 
        hundred_digit = numbers.get(hundred_digit)
        one_digit = num%10
        one_digit = numbers.get(one_digit)
        tens_digit = num//10
        tens_digit = tens_digit%10
        tens_digit = tens_digit*10
        tens_digit = numbers.get(tens_digit)
       
        result = hundred_digit+ "  " + "hundred" + " " + tens_digit+ " " + one_digit
        print(result)









