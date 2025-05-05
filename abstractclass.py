# Write a program to create a base class that consists of two functions - one to display a value, and another function is an abstract method. Next, create a subclass that consists of a method similar to the abstract method. Finally, showcase how Abstraction is being implemented in this example.
from abc import ABC,abstractmethod
class base(ABC):
    def function1(self,a):
        self.a=a
        print("Passed value is",self.a)
    @abstractmethod
    def function2(self):
        print("This is abstraction method")
class Child(base):
    def function2(self):
        print("This child function")
obj = Child()
obj.function2()
obj.function1(5)
