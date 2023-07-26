from datetime import datetime

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 0
        self.loan_amount = 0
        self.loan_taken = False
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
        else:
             print("Insufficient funds. The bank is bankrupt.")

    def check_balance(self):
        return self.balance   
    
    def transfer(self, receiver, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            receiver.balance += amount
            timestamp = datetime.now()
            self.transaction_history.append(f"Transfer amount : {amount}-Timestamp: {timestamp}")
            receiver.transaction_history.append(f"Received amount: {amount} - Timestamp: {timestamp}")
        else: 
            print("Insufficient funds.")
    
    def view_transaction_history(self):
        for transaction in self.transaction_history:
            print(transaction)
  
    def take_loan(self):
        if not self.loan_taken:
            total_amount = self.balance * 2
            self.balance += total_amount
            self.loan_amount = total_amount
            self.loan_taken = True
        else:
            print("Loan already taken.")

class Admin:
    def __init__(self):
        self.accounts = {}
        self.total_loan_amount = 0
        self.loan_feature_enabled = False

    def create_account(self, account_number, initial_balance=0):
        self.accounts[account_number] = initial_balance

    def get_account_balance(self, account_number):
        return self.accounts.get(account_number, "Account not found.")

    def check_total_available_balance(self):
        return sum(self.accounts.values())

    def enable_loan_feature(self):
        self.loan_feature_enabled = True

    def disable_loan_feature(self):
        self.loan_feature_enabled = False

def main():
    admin = Admin()
    admin.create_account("1233532", initial_balance=1000)
    balance = admin.get_account_balance("1233532")
    print("Account balance:", balance)

if __name__ == "__main__":
    main()

