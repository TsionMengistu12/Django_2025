###### question number 6

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return f"{self.name}'s yearly salary is {self.salary * 12}"

e = Employee("Tsion", 330)
print(e.annual_salary())

###### question number 7

class Library:
    def __init__(self):
        self.book_list = []

    def add_book(self, book):
        self.book_list.append(book)

    def show_book(self):
        try:
            return self.book_list
        except Exception:
            return "There are no books in the book list"

b = Library()
b.add_book("Franny and Zoey")
print(b.show_book())

####### question number 8

class Animal:
    def make_sound(self):
        print("hello") 
    
class Cat (Animal):
    def make_sound(self):
        super().make_sound()
        print("meow")
    
c = Cat()
c.make_sound()
child = Animal()
child.make_sound()
        
####### question number 9

class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def info(self):
        return f"this is a {self.brand} and it was made at {self.year}"

class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model

    def info(self):
        return f"this is a {self.brand} and it was made at {self.year} and its model is {self.model}"

v = Vehicle("BMW", 1998)
print(v.info())

c = Car("rt56", 1234, "howhh")
print(c.info())

####### question number 10

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, out):
        if self.__balance < out:
            print("your balance is insufficient")
            return 
        else:
            self.balance -= out

    def get_balance(self):
        return f"your current balance is {self.__balance}"

b = BankAccount(56)
b.deposit(12)
print(b.get_balance())

b.withdraw(70)
print(b.get_balance())

