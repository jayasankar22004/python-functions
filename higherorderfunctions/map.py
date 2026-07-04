#add 5 t0 every element
l=[[1,2],[3,4],[5,6]]
m=list(map(lambda sublist:list(map(lambda x:x+5,sublist)),l))
print(m)
#ASCII values
str='Hello'
n=list(map(ord,str))
print(n)
#memory address
h=[10,350,10,350,20]
p=list(map(id,h))
print(p)
#sqeare
a=[5,10,15,20,25,30]
b=list(map(lambda x:x**2 ,a))
print(b)
#sum of lists
c=[1,2,3,4]
d=[10,20,30]
e=list(map(lambda x,y:x+y,c,d))
print(e)

