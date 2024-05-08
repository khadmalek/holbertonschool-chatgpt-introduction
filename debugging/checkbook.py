#!/usr/bin/python3

class Checkbook:
    """
    Represents a checkbook with basic functionalities such as deposit, withdrawal, and balance inquiry.
    """
    def __init__(self):
        """
        Initializes the checkbook with a balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits the specified amount into the checkbook balance.

        Parameters:
        - amount (float): The amount to be deposited.

        Prints a message indicating the deposit amount and the current balance.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the checkbook balance if sufficient funds are available.

        Parameters:
        - amount (float): The amount to be withdrawn.

        Prints a message indicating the withdrawal amount and the current balance.
        Prints an error message if the withdrawal amount exceeds the available balance.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Prints the current balance of the checkbook.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Main function to interact with the Checkbook class.

    Allows the user to perform deposit, withdrawal, or balance inquiry operations.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $")) # add error handling with try-except
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid numeric amount.") # Display an error message if the input is not a valid number
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $")) # Add error handling with try-except
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid numeric amount.") # Display an error message if the input is not a valid number
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
    
