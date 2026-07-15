class Student:
    total_students = 0

    def __init__(self, rollno, name, marks):
        self.rollno = rollno
        self.name = name
        self.marks = marks
        Student.total_students += 1

    @staticmethod
    def is_valid_marks(marks):
        return isinstance(marks, int) and 0 <= marks <= 100

    @classmethod
    def get_total_students(cls):
        return cls.total_students

    def grade_marks(self):
        if 90 <= self.marks <= 100:
            return "A+"
        elif 80 <= self.marks <= 89:
            return "A"
        elif 70 <= self.marks <= 79:
            return "B"
        elif 60 <= self.marks <= 69:
            return "C"
        elif 40 <= self.marks <= 59:
            return "D"
        else:
            return "Fail"

    def update_marks(self, marks):
        self.marks = marks

    def display_details(self):
        grade = self.grade_marks()
        print(f"Roll No: {self.rollno} | Name: {self.name} | Marks: {self.marks} | Grade: {grade}")