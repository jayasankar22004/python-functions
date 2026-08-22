marks={
    "Rahul":85,
    "Anil":32,
    "Priya":76,
    "Sneha":45,
    "Kiran":28
}
result={ name:"Distinction" if mark>=75
         else "Pass" if mark>=40
         else "Fail" for name,mark in marks.items()}
print(result)