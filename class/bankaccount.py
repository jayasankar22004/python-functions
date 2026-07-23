class BankAccount:
    bank_name = "State Bank"
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance
    def deposit(self, amount):
        if BankAccount.validate_amount(amount):
            self.balance += amount
            print(amount, "deposited successfully.")
            print("Current Balance:", self.balance)
        else:
            print("Invalid deposit amount.")
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name
    @staticmethod
    def validate_amount(amount):
        return amount > 0
acc1 = BankAccount("Rahul", 5000)
print("Bank Name:", BankAccount.bank_name)
acc1.deposit(2000)
acc1.deposit(-500)
BankAccount.change_bank_name("Indian Bank")
print("Updated Bank Name:", BankAccount.bank_name)