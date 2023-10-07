class BankAccount:
    def __init__(self, account_number, password, balance=0):
        self.account_number = account_number
        self.password = password
        self.balance = balance

    def cash_withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrawn {amount} successfully. Updated balance: {self.balance}"
        else:
            return "Insufficient funds."

    def cash_credit(self, amount):
        self.balance += amount
        return f"Amount {amount} credited. Updated balance: {self.balance}"

    def change_password(self, new_password):
        self.password = new_password
        return "Password changed successfully."
def main():
    account = BankAccount(account_number='1234567890', password='password123', balance=1000)
    print("1. Cash Withdraw")
    print("2. Cash Credit")
    print("3. Change Password")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter the amount to withdraw: "))
        print(account.cash_withdraw(amount))
    elif choice == 2:
        amount = float(input("Enter the amount to credit: "))
        print(account.cash_credit(amount))
    elif choice == 3:
        new_password = input("Enter your new password: ")
        print(account.change_password(new_password))
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
