students = {
    "Rahul": 75,
    "Anil": 32,
    "Priya": 56,
    "Sneha": 28
}
result = {name: "Pass" if marks >= 40 else "Fail" for name, marks in students.items()}
print(result)