####### question number 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Tsion", 21)
print("name:", p.name, "\nage:", p.age, )

######## question number 2

class Dog:
    def bark(self):
        print("Woof")
    
d = Dog()
d.bark()

######## question number 3

class Car:
    def __init__(self, make):
        self.make = make

    def get_make(self):
        return f"This is the make of the car {self.make}"
        
in_make = input("Enter the make of the car ")
c = Car(in_make)
print(c.get_make())


######## question number 4
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        print("Area:", width * height) 

r = Rectangle(6, 5)
## other method
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     @property
#     def area(self):
#         return self.width * self.height
# rect = Rectangle(3,2)
# print(rect.area)
## other method
# class Rectangle:
#     @staticmethod
#     def area(width, height):
#         return width * height
    
# print(Rectangle.area(3,2))

##### question number 5
class Student:
    def __init__(self):
        self.__grade = None

    def set_grade(self, grade):
        self.__grade = grade 

    def get_grade(self):
        return self.__grade
    
s = Student()
s.set_grade(78)
print(s.get_grade())

## other method
# class Student:
#     def __init__(self):
#         self.__grade = None
    
#     ## this serves as the getter
#     @property
#     def grade(self):
#         return self.__grade
    
#     @grade.setter
#     def grade(self, value):
#         self.__grade = value

# s = Student()
# s.grade = 95
# print(s.grade)