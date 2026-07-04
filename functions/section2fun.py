def mul(a,b,c):
    return a*b*c
def describe_pet(animal,name):
    return f'My {animal} is named {name}'
def power(base,exponent):
    return base**exponent
def full_name(first,middle,last):
    return first+middle+last
que_no=int(input('enter que_no between 1-4:'))
if(que_no==1):
    print(mul(10,5,8))
elif(que_no==2):
    print(describe_pet('dog','pappy'))
elif(que_no==3):
    print(power(5,8))
elif(que_no==4):
    print(full_name('mandapati','jaya','sankar'))
else:
    print('invalid que_no')