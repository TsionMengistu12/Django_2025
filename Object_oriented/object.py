# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         return f"I'm {self.name}, {self.age} years old"
        

# p = Person("Tsion", 21)
# print(p.introduce())

class Student:
    def __init__(self, grade):
        self.__grade = grade

    def set_grade(self, in_grade):
        self.__grade = in_grade

    def get_grade(self):
        return f"this is your grade {self.__grade}"
    
in_grade = int(input("please enter grade "))
s = Student(in_grade)

# s.set_grade()
print(s.get_grade())

