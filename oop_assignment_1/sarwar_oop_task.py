class BankAccount:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New Balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print(f"Insufficient funds! Current Balance: ${self.balance:.2f}")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. Remaining Balance: ${self.balance:.2f}")

    def check_balance(self):
        print(f"Account ({self.account_number}) Balance: ${self.balance:.2f}")
        return self.balance

    def display_info(self):
        print("--- Account Details ---")
        print(f"Account Number: {self.account_number}")
        print(f"Holder Name:    {self.holder_name}")
        print(f"Balance:        ${self.balance:.2f}")
        print("-----------------------")

    def transfer(self, target_account, amount):
        print(f"\nInitiating transfer of ${amount:.2f} to {target_account.holder_name}...")
        if amount <= 0:
            print("Transfer amount must be positive.")
        elif amount > self.balance:
            print(f"Transfer failed: Insufficient balance (${self.balance:.2f}).")
        else:
            self.balance -= amount
            target_account.balance += amount
            print(f"Transfer successful! Your new balance: ${self.balance:.2f}")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance=0.0, interest_rate=0.05):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: ${interest:.2f} at rate {self.interest_rate * 100:.1f}%. New Balance: ${self.balance:.2f}")

    def display_savings_info(self):
        self.display_info()
        print(f"Interest Rate:  {self.interest_rate * 100:.1f}%")
        print("-----------------------")


# --- Demonstration / Usage Example ---
if __name__ == "__main__":
    print("=== Creating Regular Bank Account ===")
    account1 = BankAccount("ACC-101", "Sarwar", 500.0)
    account1.display_info()

    account1.deposit(200.0)
    account1.withdraw(150.0)
    account1.check_balance()

    print("\n=== Creating Savings Account (Inheritance) ===")
    savings = SavingsAccount("SAV-202", "Alex", 1000.0, interest_rate=0.04)
    savings.display_savings_info()

    savings.apply_interest()
    savings.transfer(account1, 300.0)

    account1.check_balance()
    savings.check_balance()
    savings.check_balance()