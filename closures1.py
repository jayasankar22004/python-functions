def multiply(x):
    def inner(y):
        return x*y
    return inner
k=multiply(25)
l=multiply(70)
print(k(30))
print(l(20))
