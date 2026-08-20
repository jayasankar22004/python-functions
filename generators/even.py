def even(n):
    for i in range(1,n+1):
        if(i%2==0):
            yield i
x=even(25)
print(next(x))
print(next(x))
print(next(x))