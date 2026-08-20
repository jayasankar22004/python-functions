def square(n):
    for i in n:
        yield i**2
n=[2,3,4,5,6]
for j in square(n):
    print(j)