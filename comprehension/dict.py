numbers = [10, 15, 20, 25, 30, 35]
greater_than_20 = (i for i in numbers if i > 20)
for i in greater_than_20:
    print(i)