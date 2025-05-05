# Write a program to implement abstraction on animal class (base class). The abstract method will be move will display what subclasses can do. Subclasses can be something like - Human, Dog.
from abc import ABC,abstractmethod
class base(ABC):
    def move(self):
        pass
class human(base):
    def move(self):
        print("I walk and run")
class dog(base):
    def move(self):
        print("I walk,run and bark")
obj1 = human()
obj2 =dog()
obj1.move()
obj2.move()
