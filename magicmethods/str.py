class Emp:
    def __init__(self,n,sal,e):
        self.name=n
        self.salary=sal
        self.exp=e
    def __str__(self):
        return f'name:{self.name}'
e1=Emp('jaya',120000,5)
print(e1)