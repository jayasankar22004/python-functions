'''n=int(input('enter a number:'))
m=int(input('enter a  number:'))
count=0
for i in range(n,m):
    if(i%2==0):
       count=count+1
print(f'count:{count})'''
'''n=int(input('enter a number:'))
m=int(input('enter a  number:'))
for i in range(n,m):
    if(i%4==0):
        print(i)'''
'''n=int(input('enter a number:'))
m=int(input('enter a  number:'))
sum=0
for i in range(n,m+1):
    if(i%2==0):
        sum=sum+i
print(f'sum:{sum})'''
'''n=int(input('enter a number:'))
m=int(input('enter a  number:'))
sum=0
count=0
for i in range(n,m):
    if(i%2==0):
        count=count+1
        sum=sum+i
        avg=sum/count
print(f'avg:{avg})'''
'''n=int(input('enter a number:'))
m=int(input('enter a  number:'))
count=0
for i in range(n,m):
    if(i%2==1):
        count=count+1
        print(i)
print(f'count:{count}')'''
'''n=int(input('enter a number:'))
m=int(input('enter a  number:'))
sum=0
for i in range(n,m+1):
    square=i**2
    sum=sum+square
print(f'sum:{sum}')'''
n=int(input('enter a number:'))
if(n==3):
    print('A,B,A,B,A,B')