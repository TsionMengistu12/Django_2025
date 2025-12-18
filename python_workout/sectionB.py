########## question number 4

class Teacher():
    def work(self):
        print("I teach")

class Doctor():
    def work(self):
        print("I help the sick")

works = [Teacher(), Doctor()]

for w in works:
    w.work()

############ question number 5

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Wooof Woooof .....")
        
class Cat(Animal):
    def make_sound(self):
        print("Meoooow Meoooow .....")

d = Dog()
d.make_sound()

c = Cat()
c.make_sound()

animal = [Dog(), Cat()]
for a in animal:
    a.make_sound()


########### question number 6

class Transport(ABC):

    @abstractmethod
    def move(self):
        pass

class Bus(Transport):

    def move(self):
        print("Bus moves on the road")

class Train(Transport):

    def move(self):
        print("Train moves on the tracks")

