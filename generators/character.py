def char(n):
    for i in reversed(n):
        yield i
for j in char('Sankar'):
    print(j)

