"""
Adam
Date: April 6th, 2023
Lab 10: ATM
"""

class ATM:
    def __init__(self):
        self.balance = 0  # Starting balance of $0
        self.interest_rate = 0.001  # Interest rate of 0.1%
        self.account = []
    def check_balance(self):
        """returns the account balance"""
        return self.balance

    def deposit(self, amount):
        """deposits the given amount in the account"""
        self.balance += amount
        self.account.append(f"You deposited {amount} into your account")


    def check_withdrawal(self, amount):
        """returns true if the withdrawn amount won't put the account balance in the negative"""
        if self.balance >= amount:
            return True
        else:
            return False

    def withdraw(self, amount):
        """withdraws the amount from the account and returns it"""
        self.balance -= amount
        return amount

    def calc_interest(self):
        """returns the amount of interest calculated on the account"""
        amount = self.interest_rate * self.balance
        return amount
         

atm = ATM()  # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    match command:
        case 'balance':
            balance = atm.check_balance()  # call the check_balance() method
            print(f'Your balance is ${balance}')
        case 'deposit':
            amount = float(input('How much would you like to deposit? '))
            atm.deposit(amount)  # call the deposit(amount) method
            print(f'Deposited ${amount}')
        case 'withdraw':
            amount = float(input('How much would you like '))
            # call the check_withdrawal(amount) method
            if atm.check_withdrawal(amount):
                atm.withdraw(amount)  # call the withdraw(amount) method
                print(f'Withdrew ${amount}')
            else:
                print('Insufficient funds')
        case 'interest':
            amount = atm.calc_interest()  # call the calc_interest() method
            atm.deposit(amount)
            print(f'Accumulated ${amount} in interest')
        case 'help':
            print('Available commands:')
            print('balance  - get the current balance')
            print('deposit  - deposit money')
            print('withdraw - withdraw money')
            print('interest - accumulate interest')
            print('exit     - exit the program')
        case 'exit':
            break
        case _:
            print('Command not recognized')