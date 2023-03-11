'''
Notes: Loops
Date: Mar 9, 2023
'''

counter = 0
while counter < 5:
    counter += 1
    if counter ==2:
        continue # if break, would only count to 1
    print(counter) # continue - 1 3 4 5

# else can be used with while and for
counter = 0
while counter < 5:
    counter += 1
    print(counter)
else:
    print('The loop has completed') # only occurs when while loop condition becomes False
# possible to break before the else statement, never triggering else
