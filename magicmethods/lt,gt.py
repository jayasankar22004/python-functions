class Student:
    def __init__(self,n,m,i):
        self.name=n
        self.marks=m
        self.Id=i
    def __gt__(self,other):
        return self.marks > other.marks
    def __lt__(self,other):
        return self.marks < other.marks
    def __eq__(self, other):
        return self.marks == other.marks
    def __hash__(self):
        return hash(self.Id)
    def __repr__(self):
        return self.name
s1=Student('jaya',95,25)
s2=Student('sankar',100,30)
s3=Student('sai',85,35)
s={s1,s2,s3}
print(s1)


