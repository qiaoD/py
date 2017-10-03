# #class in python

#  class -> object
# class = class variable + instance variable + method

class Student:

    prec_rise = 1.05
    
    def __init__(self, first, last, marks):
        self.first = first
        self.last  = last
        self.marks = marks
        self.email = first + '.' + last + '@123.com'

    def fullname(self):
        
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):

        self.marks = int(self.marks * 1.05)

std_1 = Student('neel','verma',55)
std_2 = Student('qiao','dong',65)

print(std_1.fullname())
print(std_2.fullname())

print(std_2.__dict__)


# inheritance

class Dumb (Student):

    perc_rise = 1.10

    def __init__(self,first,last,marks,prog_lang):
        super().__init__(first,last,marks)
        self.prog_lang = prog_lang

Stud_3 = Dumb('nesel','verma',55,1)
print(help(Stud_3))


# absract class
# cannot be instanced,it can only be inherited

from abc import ABC, abstractmethod

class Employee(ABC):

    def calculate_salary(self, sal):

        pass

class Developer(Employee):

    def calculate_salary(self,sal):

        fin = sal*1.10
        return fin

em = Developer()

