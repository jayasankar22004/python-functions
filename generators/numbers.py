def num(n):
    for i in range(1,n+1):
        yield i
x=num(25)
print(next(x))
print(next(x))
print(next(x))