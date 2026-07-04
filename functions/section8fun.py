#cube
cube=lambda x:x**3
print(cube(3))
#large number
large=lambda x,y:x if x>y else y
print(large(10,5))
#def even(n)
#return n%2==0 convert to lambda
even = lambda n:n%2==0
print(even(8))
print(even(13))
#inside lambda
def square(x):
    return x*x
result=lambda n:square(n)
print(result(6))
#.sort
fru=[(1,'banana'),(2,'apple'),(3,'cherry')]
fru.sort(key=lambda x:x[1])
print(fru)