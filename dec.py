#simple decorator
from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print('Function is starting')
        func(*args,**kwargs)
        print('Function is done')
    return wrapper
@my_decorator
def greet():
    print('Hello!')
greet()
#functools.wraps
def decorator(func):
    @wraps(func)
    def wrapper():
        print('Running')
        func()
    return wrapper
@decorator
def hello():
    pass
print(hello.__name__)
#validate positive decorator
from functools import wraps
def validate_positive(func):
    @wraps(func)
    def wrapper(*args):
        for i in args:
            if i<0:
                print('Error: Negative argument found')
                return None
        return func(*args)
    return wrapper
@validate_positive
def multiply(a,b):
    return a*b
print(multiply(3,5))
print(multiply(-3,7))
#repeat n times
