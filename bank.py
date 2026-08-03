from abc import ABC, abstractmethod

# Abstract Class
class Person(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def display(self):
        pass


# Parent Class
class BankAccount(Person):

    total_account = 0

    def __init__(self, name, account_no, balance):
        super().__init__(name)
        self.account_no = account_no
        self.__balance = balance
        BankAccount.total_account += 1

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Amount cannot be negative.")

    def deposite(self, amount):
        self.__balance += amount
        print("Amount Deposited Successfully")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient Balance")
        else:
            self.__balance -= amount
            print("Amount Withdrawn Successfully")

    def check(self):
        print("Current Balance:", self.__balance)

    def display_details(self):
        print("Account Number :", self.account_no)
        print("Account Holder :", self.name)
        print("Balance        :", self.__balance)

    def display(self):
        self.display_details()

    @classmethod
    def show_total(cls):
        print("Total Accounts:", cls.total_account)

    @staticmethod
    def bank_rules():
        print("\n------ Bank Rules ------")
        print("Minimum Balance : 1000")
        print("Working Days    : Monday - Friday")
        print("Bank Hours      : 9 AM - 5 PM")
        print("Interest Rate   : 5%")
        print("Transaction Limit : 100000")


# Child Class
class SavingsAccount(BankAccount):

    def __init__(self, name, account_no, balance):
        super().__init__(name, account_no, balance)

    def display(self):
        self.display_details()


# Bank Class
class Bank:

    def __init__(self):
        self.account = {}

    def create_account(self):
        account_no = int(input("Enter Account Number: "))
        name = input("Enter Account Holder Name: ")
        balance = float(input("Enter Opening Balance: "))

        acc = SavingsAccount(name, account_no, balance)

        self.account[account_no] = acc
        print("Account Created Successfully")

    def search(self):
        account_no = int(input("Enter Account Number: "))

        if account_no in self.account:
            return self.account[account_no]
        else:
            print("Account Not Found")
            return None

    def deposite(self):
        acc = self.search()
        if acc:
            amount = float(input("Enter Deposit Amount: "))
            acc.deposite(amount)

    def withdraw(self):
        acc = self.search()
        if acc:
            amount = float(input("Enter Withdraw Amount: "))
            acc.withdraw(amount)

    def display(self):
        acc = self.search()
        if acc:
            acc.display_details()


# Object Creation
bank = Bank()

# Menu
while True:

    print("\n===== BANK MENU =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display Account")
    print("5. Bank Rules")
    print("6. Total Accounts")
    print("7. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        bank.create_account()

    elif choice == 2:
        bank.deposite()

    elif choice == 3:
        bank.withdraw()

    elif choice == 4:
        bank.display()

    elif choice == 5:
        BankAccount.bank_rules()

    elif choice == 6:
        BankAccount.show_total()

    elif choice == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")