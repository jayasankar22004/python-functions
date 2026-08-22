students = {
    "Rahul": 35,
    "Anil": 72,
    "Priya": 81,
    "Sneha": 29,
    "Kiran": 65
}
passed = { name: marks for name, marks in students.items() if marks >= 40 }
print(passed)