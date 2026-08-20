def digits(text):
    for i in text:
        if i.isdigit():
            yield i
x=digits('Sankar123')
print(next(x))
print(next(x))
print(next(x))