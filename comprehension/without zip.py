names=["Rahul","Priya","Kiran","Sneha"]
marks=[75,35,82,28]
result={names[i]: "pass" if marks[i]>=40 else "Fail" for i in range(len(names))}
print(result)