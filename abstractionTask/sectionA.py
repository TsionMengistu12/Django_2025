########## question 1

from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, base_salary):
        self.base_salary = base_salary

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return self.base_salary
    
######## question number 2
    
class PartTimeEmployee(Employee):
    def calculate_salary(self):
        return self.base_salary
    
p = PartTimeEmployee(50000)
print(p.calculate_salary())

########## question number 3

class Appliance(ABC):
    def __init__(self):
        self.switch = False
    
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class WashingMachine(Appliance):

    def turn_on(self):

        if self.switch == False:
            self.switch = True
            print("Round we go ****** ")
        else:
            print("already on")

    def turn_off(self):

        if self.switch == False:
            print("Already off ******* ")
        else:
            self.switch = False

class ApplianceError(Exception):
    pass

class AlreadyOnError(ApplianceError):
    pass

class AlreadyOffError(ApplianceError):
    pass


class Flourescent(Appliance):

    def turn_on(self):
        try:
            if self.switch:
                raise AlreadyOnError("Light is already on ....")
            self.switch = True
            print("Let there be light .... ")
        except AlreadyOnError as e:
            print(str(e))

    def turn_off(self):
        try:
            if not self.switch:
                raise AlreadyOffError("Light is already off ..... ")
            self.switch = False
            print("off you go to darkness .... ")
        except AlreadyOffError as e:
            print(str(e))
    
f = Flourescent()
f.turn_on()
f.turn_off()

w = WashingMachine()
w.turn_on()
w.turn_off()