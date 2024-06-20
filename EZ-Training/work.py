# Create a student class that holds the details like Name, USN and Marks in 5 subjects percentage and grade.
# Create 5 student object and get the data for name, usn and marks after that find the percentage and grade and store it to the class object.

class Student:
    def __init__(self, name, usn, marks):
        self.name = name
        self.usn = usn
        self.marks = marks
        self.calculate_percentage()
        self.calculate_grade()

    def calculate_percentage(self):
        total_marks = sum(self.marks)
        self.percentage = (total_marks / 500) * 100

    def calculate_grade(self):
        if self.percentage >= 90:
            self.grade = 'A'
        elif self.percentage >= 80:
            self.grade = 'B'
        elif self.percentage >= 70:
            self.grade = 'C'
        elif self.percentage >= 60:
            self.grade = 'D'
        else:
            self.grade = 'F'

    def __str__(self):
        return f"Name: {self.name}\nUSN: {self.usn}\nMarks: {self.marks}\nPercentage: {self.percentage}%\nGrade: {self.grade}"

stud1 = Student("John Doe", "USN123456", [85, 90, 78, 92, 88])
stud2 = Student("Jane Smith", "USN789012", [95, 92, 85, 90, 88])
stud3 = Student("Bob Johnson", "USN345678", [78, 85, 92, 88, 90])
stud4 = Student("Alice Brown", "USN901234", [90, 88, 92, 85, 95])
stud5 = Student("Mike Davis", "USN567890", [85, 78, 88, 92, 90])

print(stud1)
print(stud2)
print(stud3)
print(stud4)
print(stud5)