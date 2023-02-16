# class Student:
#     def __init__(self,name, salary):
#         self.name =name
#         self.__salary = salary
#
#     def __str__(self):
#         return self.name
#
#     def __repr__(self):
#         return f"Student({self.name}: {type(self.name)}, {self.__salary}: {type(self.__salary)} )"
#
# s = Student("noha", 312)
# print(s) ## user ---> level
# print(s.__repr__()) # debugging ---> development


# l = [34,46,455]
# print(l)
# print(len(l))

################################
# class Student:
#     def __init__(self,name, salary):
#         self.name =name
#         self.__salary = salary
#
#     def __str__(self):
#         return self.name
#
#     def __repr__(self):
#         return f"Student({self.name}: {type(self.name)}, {self.__salary}: {type(self.__salary)} )"
#
#     def __len__(self):
#         # return with int
#         return len(self.__dict__)
#
# s = Student("noha", 312)
# # s.country ='cairo'
# print(len(s))
# print(s.__dict__)  # represent object using __dict__ in form of dict...
#####################################
#
# class Student:
#     def __init__(self,name, salary):
#         self.name =name
#         self.__salary = salary
#
#     def __str__(self):
#         return self.name
#
#     def __repr__(self):
#         return f"Student({self.name}: {type(self.name)}, {self.__salary}: {type(self.__salary)} )"
#
#     def __len__(self):
#         # return with int
#         return len(self.__dict__)
#
#     def __call__(self, var, *args, **kwargs):
#         print(f"---- object is being called {var}-----")
# s = Student("noha", 312)
# s(98)
# s.__call__(34)
############################
class Student:
    __slots__ = ['name', '__salary', 'test']
    def __init__(self,name, salary):
        self.name =name
        self.__salary = salary
        self.test = 19


s = Student("Ahmed", 'Ali')
print(type(s))
mm = type(s)
mys = Student('Ahmed', 2234)
# mys.country = 'Egypt'
# mys.mm = '34i'
# print(mys.__dict__)


# class Student2:
#     def __init__(self,name, salary):
#         self.name =name
#         self.__salary = salary
# #
# ss= Student2("ss", 3224)
# print(ss.__dict__)



