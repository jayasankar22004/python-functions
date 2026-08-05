class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,o2):
        return (self.x+o2.x,self.y+o2.y)
    def __sub__(self,o2):
        return (self.x-o2.x,self.y-o2.y)
    def __str__(self):
        return f'vector({self.x},{self.y})'
    def __repr__(self):
        return f'vector({self.x},{self.y})'
v1=Vector(7,8)
v2=Vector(6,7)
print(v1+v2)
print(v1-v2)
print(v1)
l=[v1,v2]
print(l)