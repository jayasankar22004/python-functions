#capital letters
l='HEllo wHO arE you'
def vowels(x):
    return x not in 'AEIOUaeiou'
k=list(filter(vowels,l))
print(k)
#divisible by 5
l=[5,10,15,17,20,25]
k=list(filter(lambda x:x%5==0,l))
print(k)
#even
l=[1,2,4,5,6,7]
def even(x):
    return x%2==0
k=list(filter(even,l))
print(k)
#dictionary
d={'apple':100,'banana':40,'cherry':150}
filtered_items=filter(lambda item:item[1]>50,d.items())
result=dict(filtered_items)
print(result)