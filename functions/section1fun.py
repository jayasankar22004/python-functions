def say_hello():
    print('Welcome to Python!')
def add(a,b):
    print(f'sum of two numbers {a+b}')
def area_of_rectangle(length,width):
    return length*width
def no_return():
    m=0
question_no=int(input('enter question_no. between 1-4:'))
if(question_no==1):
    say_hello()
elif(question_no==2):
    add(10,12)
elif(question_no==3):
    print(area_of_rectangle(6,4))
elif(question_no==4):
    no_return()
else:
    print('Invalid Question')


