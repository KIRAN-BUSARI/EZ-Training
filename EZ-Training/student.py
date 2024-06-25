class Student:
    def __init__(self):
        self.USN = None
        self.name = None
        self.marks = []
        self.grade = None
        self.percentage = None

    def std_input(self):
        self.USN = input("Enter USN: ")
        self.name = input("Enter Name: ")
        for i in range(0,5):
            marks = input(f"Enter your Marks in Subject{i+1}: ")
            self.marks.append(marks)

    def cal_percentage(self):
        sum = 0
        for i in self.marks:
            sum = sum + i
            self.percentage = (sum/500)*100

    def cal_Grade(self):
        per = self.percentage
        if per <= 100 and per >= 80:
            self.grade = "A"
        elif per <= 80 and per >= 60:
            self.grade = "B"
        elif per <= 60 and per >= 40:
            self.grade = "C"
        elif per <= 40 and per >= 0:
            self.grade = "D"
        else:
            self.grade = "Invalid"

    def print_details(self):
        print("Name : " + self.name)
        print("USN : " + self.USN)
        print("Marks in 5 subjects are : ")
        for i in range(0,5):
            print(f"Subject {i+1} = {self.marks[i]}")
        print("Percentage : " + self.percentage)
        print("Grade : "+ self.grade)

st1 = Student()

st1.std_input()
st1.cal_Grade()
st1.cal_percentage()
st1.print_details()

