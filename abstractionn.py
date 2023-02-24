## abstraction ---> create basic structure ---> doesn't have any implementation

"""
    abstract class Person{
        # define properties
        abstract method1 {}
        abstract method2 {}
    }  # cannot take object from class

    class Employee extends Person{
    method1 {
    print(test);}
    }
"""


#
# class Car:
#     pass

### simulate abastraction

from abc import  ABC, abstractmethod  #Abstract Base class


# # to define abstract class ---> you must define abstract method in the class
# class Car (ABC):
#     @abstractmethod
#     def test(self):
#         pass
#
# # c= ABC()
# # print(c)
#
# cc = Car()
# print(cc)
# cc.test()

########################
# to define abstract class ---> you must define abstract method in the class
# class Car(ABC):
#     @abstractmethod
#     def test(self):
#         pass
#
# cc = Car()
# print(cc)
# cc.test()

#######################################################
# class BasicType(ABC):
#     @abstractmethod
#     def insert(self, **kwargs):
#         pass
#
#     @abstractmethod
#     def list(self):
#         pass
#
#
# class User(BasicType):
#     def insert(self, **kwargs):
#         print(kwargs)

#user her is abstract ---> as you didn't implememnt the abstract method.

##############################################
# class BasicType(ABC):
#     @abstractmethod
#     def insert(self, **kwargs):
#         pass
#
#     @abstractmethod
#     def list(self):
#         pass
#
#
# class User(BasicType):
#     def insert(self, **kwargs):
#         print(kwargs)
#
#     def list(self, message):
#         print(f"--------list  {message}")
#
# u = User()
# u.list('hiiii')

##################################
from abc import ABCMeta, ABC, abstractmethod, abstractproperty,\
    abstractclassmethod, abstractstaticmethod
# class Test(ABCMeta):
#     @abstractmethod
#     def Test(cls):
#         pass
#
# class Test2(metaclass=Test):
#     pass
#


#
# class Calculator(metaclass=ABCMeta):
#     @abstractmethod
#     def add(self):
#         pass
#
#
#     @abstractmethod
#     def subtract(self):
#         pass
#
#
# class Calculation(Calculator):
#     def __init__(self, a,b):
#         self.a=a
#         self.b = b
#
#     def add(self):
#         return self.a + self.b
#
#     def subtract(self):
#         return self.a - self.b
#
#
# c = Calculation(4,6)
# print(c.add())
# print(c.subtract())
#
#
#
#
#
#
################################


# class Calculator(ABC): # ABC is ABCMETA
#     @abstractmethod
#     def add(self):
#         pass
#
#
#     @abstractmethod
#     def subtract(self):
#         pass
#
#
# class Calculation(Calculator):
#     def __init__(self, a,b):
#         self.a=a
#         self.b = b
#
#     def add(self):
#         return self.a + self.b
#
#     def subtract(self):
#         return self.a - self.b
#
#
# c = Calculation(4,6)
# print(c.add())
# print(c.subtract())




























# class MM(ABCMeta):
#     def myl(cls):
#         pass
#
#
# class MyClass(MM):  # this abstract class
#     @ab


# mm = MyClass()
# MyClass.myl()


class SS(metaclass=ABCMeta):
    @staticmethod
    def sayHi():
        pass

class A (SS):
    def sayHi(self):
        print("-----Hiiiiiiii----")

a = A()
a.sayHi()

#
#
#
#
#
#
#
#



