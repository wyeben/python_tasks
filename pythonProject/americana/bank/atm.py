from americana.bank.account import Account


def main():
    accounts = {}

    while True:
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Display Balance")
        print("5. Exit")

        choice = int(input("Select an option: "))

        if choice == 1:

            if choice == 1:
                pin = input("Enter PIN: ")
                account_number = Account.generate_account_number()
                new_account = Account(account_number, pin)
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                new_account.register(first_name, last_name)
                accounts[new_account.get_account_number()] = new_account
                print(f"Account created! Your account number is {new_account.get_account_number()}.")

        elif choice == 2:
            account_number = input("Enter account number: ")
            if account_number in accounts:
                amount = float(input("Enter deposit amount: "))
                accounts[account_number].deposit(amount)
                print("Deposit successful!")
            else:
                print("Account not found.")

        elif choice == 3:
            account_number = input("Enter account number: ")
            if account_number in accounts:
                pin = input("Enter PIN: ")
                amount = float(input("Enter withdrawal amount: "))
                if accounts[account_number].withdraw(amount, pin):
                    print("Withdrawal successful!")
                else:
                    print("Insufficient balance or incorrect PIN.")
            else:
                print("Account not found.")

        elif choice == 4:
            account_number = input("Enter account number: ")
            if account_number in accounts:
                balance = accounts[account_number].get_balance()
                print(f"Account balance:  ₦{balance:.2f}")
            else:
                print("Account not found.")

        elif choice == 5:
            print("Exiting the bank application.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()