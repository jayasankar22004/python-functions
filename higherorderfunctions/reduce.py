#largest number
from functools import reduce
l=[12,10.25,6,35,17]
def green(x,y):
    if x>y:
        return x
    return y
k=reduce(green,l)
print(k)
#concatenate
a=['p','y','t','h','o','n']
b=reduce(lambda x,y:x+y,a)
print(b)
#sum
c=[5,10,15,20,25]
d=reduce(lambda x,y:x+y,c)
print(d)