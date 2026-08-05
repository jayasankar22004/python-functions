#shallow copy
a=[[1,2],[3,4]]
import copy
b=copy.copy(a)
b[0][0]=20
print(a)
print(b)
#deepcopy
d=[[10,20],[30,40]]
c=copy.deepcopy(d)
c[0][0]=50
print(d)
print(c)
