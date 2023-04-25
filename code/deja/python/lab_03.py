'''
Lab 3: Pick6
14 Mar 23
'''

#Generate a list of 6 random numbers representing the winning tickets
import random

cpu = []                            # emtpy list to store random numbers
for x in range(0,6):                # setting the range of 6 numbers        
    c = random.randint(1,99)        # variable to store randint module 
    cpu.append(c)                   # enabling empty list to access randint within  set range (6)            
    

balance = 0                         # counter to hold a collective value

for x in range(100000):             # sets the loop in its entirety
    balance = balance - 2           # counter - cost of initial ticket purchase

    winningticket = []              # generates the winning ticket values
    for x in range(0,6):
        t = random.randint(1,99)
        winningticket.append(t)
    
    matches = 0                             # evaluating how many matches within the given range
    for x in range(6):
        if cpu[x] == winningticket[x]:       
            matches = matches + 1
    print(f" We have {matches} match(es)!")

    if matches == 1:                        # determining how many matches we have
        balance = balance + 4               # within the range of values available on
    elif matches == 2:                      # purchased tickets vs winning ticket
        balance = balance + 7
    elif matches == 3:
        balance = balance + 100
    elif matches == 4:
        balance = balance + 50000
    elif balance == 5:
        balance = balance +1000000
    elif balance == 6:
        balance = balance + 25000000
    print(balance)

# VERSION 2
# The ROI (return on investment) is defined as (earnings - expenses)/expenses. Calculate your ROI, 
# print it out along with your earnings and expenses.

roi = (balance/200000)/200000
print(roi)




#a ticket costs $2
#if 1 number matches, you win $4
#if 2 numbers match, you win $7
#if 3 numbers match, you win $100
#if 4 numbers match, you win $50,000
#if 5 numbers match, you win $1,000,000
#if 6 numbers match, you win $25,000,000





#Start your balance at 0
#Loop 100,000 times, for each loop:
#Generate a list of 6 random numbers representing the ticket
#Subtract 2 from your balance (you bought a ticket)
#Find how many numbers match
#Add to your balance the winnings from your matches
#After the loop, print the final balance