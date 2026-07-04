#multiplication
def multiply_all(*args):
    total=1
    for num in args:
        total*=num
    return total
print(multiply_all(10,2,4,5))
#display tags
def display_tags(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}:{value}')
display_tags(name='middle',age=21,city='chirala')
#hobbies
def describe_hobbies(name,*hobbies):
    print(f'name:{name},hobbies{hobbies}')
describe_hobbies('jaya sankar','reading','gaming',)
#output
def f(*args):
    print(type(args))
f(1,2,3)
#mixed
def mixed(a,b,*args,**kwargs):
    print(f'a:{a},b:{b},args:{args},kwargs:{kwargs}')
mixed(1,3,4,5,6,7,x=25,y=35)