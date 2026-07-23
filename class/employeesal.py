class Employee:
    bonus_rate = 0.1
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    def final_salary(self):
        return self.base_salary + (self.base_salary *self.bonus_rate)
    @classmethod
    def update_bonus(cls, new_rate):
        cls.bonus_rate = new_rate
    @staticmethod
    def is_valid_salary(sal):
        return sal > 0
emp1 = Employee("Hari", 50000)
emp2 = Employee("Sumanth", 60000)
print("Salary Validity:")
print(emp1.name, ":", Employee.is_valid_salary(emp1.base_salary))
print(emp2.name, ":", Employee.is_valid_salary(emp2.base_salary))
print("Before Updating Bonus:")
print(emp1.name, "Final Salary =", emp1.final_salary())
print(emp2.name, "Final Salary =", emp2.final_salary())
Employee.update_bonus(0.2)
print("After Updating Bonus:")
print(emp1.name, "Final Salary =", emp1.final_salary())
print(emp2.name, "Final Salary =", emp2.final_salary())