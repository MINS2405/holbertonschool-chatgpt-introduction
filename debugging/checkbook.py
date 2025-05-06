class Checkbook:
"""
Class Description:
The Checkbook class simulates a simple checkbook for managing deposits, withdrawals, and balance inquiries.
It allows users to deposit funds, withdraw funds, and check their current balance.
"""

def __init__(self):
"""
Initializes the Checkbook with a balance of 0.0.
"""
self.balance = 0.0

def deposit(self, amount):
"""
Adds the specified amount to the balance.

Parameters:
amount (float): The amount to deposit.

Returns:
None
"""
self.balance += amount
print("Deposited ${:.2f}".format(amount))
print("Current Balance: ${:.2f}".format(self.balance))
def withdraw(self, amount):
"""
Deducts the specified amount from the balance if there are sufficient funds.

Parameters:
amount (float): The amount to withdraw.

Returns:
None
"""
if amount > self.balance:
print("Insufficient funds to complete the withdrawal.")
else:
self.balance -= amount
print("Withdrew ${:.2f}".format(amount))
print("Current Balance: ${:.2f}".format(self.balance))

def get_balance(self):
"""
Prints the current balance.

Returns:
None
"""
print("Current Balance: ${:.2f}".format(self.balance))


def main():
"""
The main function runs the interactive checkbook application.It handles user input and performs corresponding checkbook operations (deposit, withdraw, balance, exit).
Includes error handling to prevent crashes from invalid inputs.
"""
cb = Checkbook()
while True:
action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
if action == 'exit':
break
elif action == 'deposit':
try:
amount = float(input("Enter the amount to deposit: $"))
cb.deposit(amount)
except ValueError:
print("Invalid input. Please enter a numeric value.")
elif action == 'withdraw':
try:
amount = float(input("Enter the amount to withdraw: $"))
cb.withdraw(amount)
except ValueError:
print("Invalid input. Please enter a numeric value.")
elif action == 'balance':
cb.get_balance()
else:
print("Invalid command. Please try again.")


# Run the program
if __name__ == "__main__":
main()

factorial.py
#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n to avoid infinite loop
    return result

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            input_number = int(sys.argv[1])
            if input_number < 0:
                print("Factorial is not defined for negative numbers.")
            else:
                print(factorial(input_number))
        except ValueError:
            print("Please provide a valid integer as input.")
    else:
        print("Usage: ./factorial.py <number>")