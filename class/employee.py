class Employee:
    company_name = "TechCorp"
    def __init__(self, name):
        self.name = name
    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name
e1 = Employee("Sankar")
e2 = Employee("Siva")
print(e1.name, "-", e1.company_name)
print(e2.name, "-", e2.company_name)
Employee.change_company("cv corp")
print("after change:")
print(e1.name, "-", e1.company_name)
print(e2.name, "-", e2.company_name)