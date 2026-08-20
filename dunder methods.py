#book
class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def __str__(self):
        return f'{self.title} by {self.author} Rs: {self.price}'
    def __repr__(self):
        return f'Book({self.title},{self.author},{self.price})'
b1=Book('Classmet','Sankar',30)
print(b1)
print(repr(b1))
#vector
class Vector2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self, other):
        return self.x+other.x,self.y+other.y
    def __sub__(self, other):
        return self.x-other.x,self.y-other.y
    def __mul__(self, other):
        return self.x*other.x,self.y*other.y
    def __truediv__(self, other):
        return self.x/other.x,self.y/other.y
    def __floordiv__(self, other):
        return self.x//other.x,self.y//other.y
    def __mod__(self, other):
        return self.x%other.x,self.y,other.y
v1=Vector2D(3,4)
v2=Vector2D(5,5)
print(v1+v2)
print(v1-v2)
print(v1*v2)
print(v1/v2)
print(v1//v2)
print(v1%v2)
#temperature
class Temperature:
    def __init__(self, celsius):
            self.celsius = celsius
    def __lt__(self, other):
            return self.celsius < other.celsius
    def __le__(self, other):
            return self.celsius <= other.celsius
    def __gt__(self, other):
            return self.celsius > other.celsius
    def __ge__(self, other):
            return self.celsius >= other.celsius
    def __eq__(self, other):
            return isinstance(other, Temperature) and self.celsius == other.celsius
    def __hash__(self):
            return hash(self.celsius)
    def __repr__(self):
            return f'Temperature({self.celsius})'
print(Temperature(100) > Temperature(50))
temps_list = [Temperature(30), Temperature(10), Temperature(20)]
sorted_temps = sorted(temps_list)
print('Sorted:', sorted_temps)
temps_set = {Temperature(100), Temperature(50), Temperature(100)}
print('Set:', temps_set)
