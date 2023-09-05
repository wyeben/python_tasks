import tkinter as tk
from tkinter import simpledialog, messagebox
from americana.bank.account import Account


class BankAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Americana Bank Application")

        self.accounts = {}

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="AMERICANA BANK PLC", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.create_account_btn = tk.Button(self.root, text="Create Account", command=self.create_account)
        self.create_account_btn.pack()

        self.deposit_btn = tk.Button(self.root, text="Deposit", command=self.deposit)
        self.deposit_btn.pack()

        self.withdraw_btn = tk.Button(self.root, text="Withdraw", command=self.withdraw)
        self.withdraw_btn.pack()

        self.display_balance_btn = tk.Button(self.root, text="Display Balance", command=self.display_balance)
        self.display_balance_btn.pack()

        self.exit_btn = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_btn.pack()

    def create_account(self):
        pin = simpledialog.askinteger("Create Account", "Enter PIN:")
        account_number = Account.generate_account_number()
        new_account = Account(account_number, pin)
        first_name = simpledialog.askstring("Create Account", "Enter first name:")
        last_name = simpledialog.askstring("Create Account", "Enter last name:")
        new_account.register(first_name, last_name)
        self.accounts[new_account.get_account_number()] = new_account
        messagebox.showinfo("Account Created", f"Account created! Your account number is"
                                               f" {new_account.get_account_number()}.")

    def deposit(self):
        account_number = simpledialog.askstring("Deposit", "Enter account number:")
        if account_number in self.accounts:
            amount = simpledialog.askfloat("Deposit", "Enter deposit amount:")
            self.accounts[account_number].deposit(amount)
            messagebox.showinfo("Deposit", "Deposit successful!")
        else:
            messagebox.showerror("Account Not Found", "Account not found.")

    def withdraw(self):
        account_number = simpledialog.askstring("Withdraw", "Enter account number:")
        if account_number in self.accounts:
            pin = simpledialog.askinteger("Withdraw", "Enter PIN:")
            amount = simpledialog.askfloat("Withdraw", "Enter withdrawal amount:")
            if self.accounts[account_number].withdraw(amount, pin):
                messagebox.showinfo("Withdrawal", "Withdrawal successful!")
            else:
                messagebox.showerror("Withdrawal Error", "Insufficient balance or incorrect PIN.")
        else:
            messagebox.showerror("Account Not Found", "Account not found.")

    def display_balance(self):
        account_number = simpledialog.askstring("Display Balance", "Enter account number:")
        if account_number in self.accounts:
            balance = self.accounts[account_number].get_balance()
            messagebox.showinfo("Balance", f"Account balance: ₦{balance:.2f}")
        else:
            messagebox.showerror("Account Not Found", "Account not found.")


if __name__ == "__main__":
    root = tk.Tk()
    app = BankAppGUI(root)
    root.mainloop()
