###### question number 6

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def annual_salary(self):
#         return f"{self.name}'s yearly salary is {self.salary * 12}"

# e = Employee("Tsion", 330)
# print(e.annual_salary())

###### question number 7

class Library:
   def __init__(self, book_list):
        self.book_list = list(book_list)



    def add_book(self,book):
        self.book_list.append(book)





