class Student:
    passing_marks = 40
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def result(self):
        if self.marks >= Student.passing_marks:
            print(self.name, "Pass")
        else:
            print(self.name, "Fail")
    @classmethod
    def update_passing_marks(cls, new_marks):
        cls.passing_marks = new_marks
    @staticmethod
    def grade_category(marks):
        if marks >= 90:
            return "A"
        elif marks >= 75:
            return "B"
        elif marks >= 40:
            return "C"
        else:
            return "Fail"
s1 = Student("Ravi", 85)
s2 = Student("Priya", 38)
print("Initial Passing Marks:", Student.passing_marks)
print(s1.name, "Grade:", Student.grade_category(s1.marks))
s1.result()
print(s2.name, "Grade:", Student.grade_category(s2.marks))
s2.result()
Student.update_passing_marks(50)
print("Updated Passing Marks:", Student.passing_marks)
s1.result()
s2.result()