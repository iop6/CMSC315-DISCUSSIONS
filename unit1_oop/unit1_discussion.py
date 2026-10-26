"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class Account:
    # class variable, every account is at the same bank
    bank_name = "Chase"

    def __init__(self, owner, balance):
        # instance variables, each account gets its own
        self.owner = owner
        self.balance = balance

    def describe(self):
        return f"{self.owner} - ${self.balance}"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class SavingsAccount(Account):
    # new class variable, every savings account needs at least $100
    min_balance = 100

    def __init__(self, owner, balance, interest_rate, transactions):
        # let Account set owner and balance so I don't repeat that code
        super().__init__(owner, balance)
        self.interest_rate = interest_rate  # as a percent, 4 means 4%
        self.transactions = transactions  # a list, used later for the copy demo

    # new method that only savings accounts have
    def add_interest(self):
        interest = self.balance * self.interest_rate // 100
        self.balance += interest
        self.transactions.append(interest)

    # overrides Account's describe() to add the savings info
    def describe(self):
        return f"{super().describe()} at {self.interest_rate}% interest, transactions: {self.transactions}"


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n--- Namespace Demonstration ---")

    acct1 = SavingsAccount("Maria", 1000, 5, [1000])
    acct2 = SavingsAccount("James", 250, 5, [250])

    # min_balance lives on the class, but the objects can still read it
    print("SavingsAccount.min_balance (through the class):", SavingsAccount.min_balance)
    print("acct1.min_balance (through an object):", acct1.min_balance)

    # add an attribute to acct1 only, acct2 won't have it
    acct1.nickname = "Vacation Fund"
    print("\nAdded nickname to acct1 only")
    print("acct1 has nickname?", hasattr(acct1, "nickname"))
    print("acct2 has nickname?", hasattr(acct2, "nickname"))

    # __dict__ only shows what is stored on that object,
    # min_balance and bank_name don't show up because they belong to the classes
    print("\nacct1.__dict__:", acct1.__dict__)
    print("acct2.__dict__:", acct2.__dict__)

    # the class namespace holds the class variables and methods
    # (skipping the built in names that start with __)
    print("\nSavingsAccount class namespace:", [name for name in SavingsAccount.__dict__ if not name.startswith("__")])
    print("Account class namespace:", [name for name in Account.__dict__ if not name.startswith("__")])


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n--- Copy Demonstration ---")

    # the transactions list is the nested mutable data
    original = SavingsAccount("David", 800, 3, [500, 300])

    # shallow copy makes a new account, but it points to the SAME transactions list
    shallow = copy(original)

    # deep copy makes a new account AND a brand new transactions list
    deep = deepcopy(original)

    print("Before changing the original:")
    print("Original:", original.transactions)
    print("Shallow: ", shallow.transactions)
    print("Deep:    ", deep.transactions)

    # add a $200 withdrawal to the original's list
    original.transactions.append(-200)

    print("\nAfter adding a -200 withdrawal to the original:")
    print("Original:", original.transactions)
    print("Shallow: ", shallow.transactions)
    print("Deep:    ", deep.transactions)

    # the shallow copy changed too because it shares the list,
    # the deep copy didn't because it has its own list
    print("\nSame list in original and shallow?", original.transactions is shallow.transactions)
    print("Same list in original and deep?", original.transactions is deep.transactions)


# ---------- MY EXTENSION: ONE CUSTOMER, DIFFERENT ACCOUNTS ----------
# a customer can have different kinds of accounts,
# and each one uses its own version of describe()

class CheckingAccount(Account):
    monthly_fee = 5

    def __init__(self, owner, balance, overdraft_limit):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def describe(self):
        return f"{super().describe()}, can overdraft up to ${self.overdraft_limit}"


def demonstrate_customer_accounts(basic, savings):
    print("\n--- Extension: All of Isaac's Accounts ---")

    # reuse the two accounts from main and add a checking account
    checking = CheckingAccount("Isaac", 300, 100)
    accounts = [basic, savings, checking]

    # same method call, but each class gives a different answer
    for account in accounts:
        print(type(account).__name__ + ":", account.describe())

    # all of them get bank_name from Account without writing it again
    print("\nAll at", checking.bank_name + "?", all(a.bank_name == "Chase" for a in accounts))
    print("Total money:", "$" + str(sum(a.balance for a in accounts)))


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("--- Unit 1 OOP Assignment ---")

    print("\n--- Parent Object ---")
    basic = Account("Isaac", 200)
    print("Account:", basic.describe())
    print("Bank:", basic.bank_name)

    print("\n--- Child Object ---")
    savings = SavingsAccount("Isaac", 1000, 4, [1000])
    print("SavingsAccount:", savings.describe())
    savings.add_interest()
    print("After add_interest:", savings.describe())

    # SavingsAccount never defines bank_name or owner, it gets them from Account
    print("Inherited bank_name:", savings.bank_name)
    print("Inherited owner:", savings.owner)
    print("Is savings an Account?", isinstance(savings, Account))

    demonstrate_namespaces()
    demonstrate_copying()
    demonstrate_customer_accounts(basic, savings)


if __name__ == "__main__":
    main()
