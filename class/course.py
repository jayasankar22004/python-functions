class Course:
    total_students = 0   # Class variable
    def __init__(self, student_name):
        self.student_name = student_name   # Instance variable
    def enroll(self):
        Course.total_students += 1
        print(self.student_name, "has enrolled.")
    @classmethod
    def show_total(cls):
        print("Total Students Enrolled:", cls.total_students)
    @staticmethod
    def is_eligible(age):
        return age >= 18
print("Eligibility:", Course.is_eligible(20))
s1 = Course("Ravi")
s2 = Course("Priya")
s3 = Course("Anil")
s1.enroll()
s2.enroll()
s3.enroll()
Course.show_total()