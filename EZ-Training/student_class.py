# """This is class demo on day 2"""
# class Student :
#     """Class creating a student"""
#     def __init__(self,nm,ag,gen):
#         self.name = nm
#         self.age = ag
#         self.gender = gen

# # 1st Way
# st1 = Student("Kiran",20,"M")
# print(st1.name,st1.age,st1.gender,sep="\n")

# # 2nd Way
# n = input("Enter name :")
# a = int(input("Enter Age :"))
# g = input("Enter Gender : ")

# st2 = Student(n,a,g)
# print(st2.name,st2.age,st2.gender,sep="\n")

# # 3rd Way

# print(type(st2))
# print(type(a))
# print(type(n))
# print(type(g))


class A:
    def __init__(self,a,b):
        self.A = a
        self.B = b
    
    def printB(self):
        print(self.B)

ob1 = A(12,2)

print(ob1.A,ob1)
