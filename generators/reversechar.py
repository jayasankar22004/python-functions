def char(text):
    for i in text:
        yield i
x=char('Sankar')
print(next(x))
print(next(x))
print(next(x))


