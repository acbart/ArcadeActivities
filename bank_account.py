# SafeAccount - cannot be overdrawn

# Bank accounts have a name and a balance
class BankAccount:
    name: str
    balance: int

    def __init__(self, the_name_of_the_account: str, initial_balance: int):
        self.name = the_name_of_the_account
        self.balance = initial_balance

    def deposit(self, amount: int):
        self.balance += amount

    def withdraw(self, amount: int) -> int:
        if amount > self.balance:
            old_balance = self.balance
            self.balance = 0
            return old_balance
        else:
            self.balance -= amount
            return amount



dr_barts_points = BankAccount("UD Points", 100)
ellies_checking = BankAccount("M&T Checking Account", 1000000000)

dr_barts_points.deposit(200)
print(dr_barts_points.balance)

some_money = dr_barts_points.withdraw(50)
print("You got", some_money, "dollars. You have a balance of", dr_barts_points.balance)

print("You got", dr_barts_points.withdraw(50), "dollars. You have a balance of", dr_barts_points.balance)

some_money = dr_barts_points.withdraw(1000)
print("You got", some_money, "dollars")