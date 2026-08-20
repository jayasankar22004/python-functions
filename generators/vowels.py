def vowels(n):
    vowel='aeiouAEIOU'
    for i in n:
        if i in vowel:
            yield i
x=vowels('Sankar')
print(next(x))
print(next(x))

