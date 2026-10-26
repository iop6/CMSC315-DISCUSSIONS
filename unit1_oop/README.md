# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.

---

## How to Run

```
python3 unit1_discussion.py
```

## How It Works

**Parent Class - `Account`**

- Class variable: `bank_name = "Chase"`, shared by every account.
- Instance variables: `owner` and `balance`, which were different for each account.
- `describe()` returned a string like `Isaac - $200`.

**Child Class - `SavingsAccount(Account)`**

- Inherited everything from `Account`.
- New class variable: `min_balance = 100`.
- New instance variables: `interest_rate` (as a percent) and `transactions` (a list).
- New method: `add_interest()` added interest to the balance and saved it in the transactions list.
- Overrode `describe()`. It called the parent's version with `super()` and added the interest rate and transactions.
- I used `super().__init__()` so `SavingsAccount` didn't have to set `owner` and `balance` again.

## Namespaces

- `SavingsAccount.min_balance` and `acct1.min_balance` both printed `100`. The value only lived on the class, but Python looked there when the object didn't have it.
- I added `nickname` to `acct1` after it was created. `acct2` didn't get it, which showed that each object had its own namespace.
- `acct1.__dict__` only showed the instance variables (and `nickname`). `min_balance` and `bank_name` weren't there because they belonged to the classes.
- The class namespace held the class variables and methods: `SavingsAccount` had `min_balance`, `add_interest`, and `describe`, and `Account` had `bank_name` and `describe`.

## Shallow vs Deep Copy

I made a `SavingsAccount` with a transactions list, then made a shallow copy and a deep copy. After adding a `-200` withdrawal to the original:

| Object   | Transactions          |
|----------|-----------------------|
| Original | 500, 300, **-200**    |
| Shallow  | 500, 300, **-200**    |
| Deep     | 500, 300              |

- **Shallow copy** made a new account, but it shared the same list as the original, so the change showed up in both.
- **Deep copy** made a new account and a new list, so it was not affected.
- Using `is` confirmed it: the original and shallow copy pointed to the same list, the deep copy did not.

## My Extension - One Customer, Different Accounts

I added a `CheckingAccount` class (another child of `Account`) with a `monthly_fee` and an `overdraft_limit`. Then I put a basic `Account`, a `SavingsAccount`, and a `CheckingAccount` for the same customer in one list and called `describe()` on each. The same method call gave a different result for each class, all of them had `bank_name` from `Account` without writing it again, and I added up the balances to get the customer's total money.

## Real-World Use

A banking app could use this setup. Shared info like the owner, balance, and bank name is written once in `Account`, and each type of account only adds what is different. Adding a new type, like a CD or a credit card account, would just be one more small child class.
