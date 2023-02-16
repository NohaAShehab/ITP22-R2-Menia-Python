# class Employee:
#     count = 0
#     def __init__(self, name, email, salary):
#         self.name = name
#         self._email = email  # protected
#         self.__salary = salary
#         Employee.count +=1
#         self.__id = Employee.count
#
#     def get_id(self):
#         return self.__id
#
#     def get_emp_id(self):
#         print(self.__abbass())
#         return self.__id
#
#     def __abbass(self):
#         return self.__id
#
#
# e = Employee("Ahmed",'Ahmed', 2034)
# e2 = Employee("Ahmed",'Ahmed', 2034)
# print(e2.get_emp_id())


# #####################################3
# class Employee:
#     count = 0
#     def __init__(self, name, email, salary):
#         self.name = name
#         self._email = email  # protected
#         # self.__salary = salary
#         Employee.count +=1
#         self.__id = Employee.count
#         # if isinstance(salary, int) or isinstance(salary, float):
#         #     self.sal = salary
#         # else:
#         #     raise  ValueError("Salary should be number")
#         if isinstance(salary, int) or isinstance(salary, float):
#             self.__salary = salary
#         else:
#             raise ValueError("Salary cannot be string")
#
#     def get_emp_id(self):
#         return self.__id
#
#     ### do operation
#     def salary(self):
#         return self.__salary
#
#     def setSalary(self, sal):
#         if isinstance(sal, int) or isinstance(sal, float):
#             self.__salary  =sal
#         else:
#             raise ValueError("Salary cannot be string")
# e = Employee("Ahmed",'Ahmed', 2034)
# e2 = Employee("Ahmed",'Ahmed', 2034)
# print(e2.get_emp_id())
# print(e2.salary())
# print(e2.setSalary("3213"))
# print(e2.salary())
############################################
#####################################3
class Employee:
    count = 0
    def __init__(self, name, email, salary):
        self.name = name
        self._email = email  # protected
        Employee.count +=1
        self.__id = Employee.count
        self.salary = salary


    @property
    def id(self):
        return self.__id


    ### do operation
    @property
    def salary(self):
        return self.__salary

    @salary.setter  # property setter
    def salary(self, sal):
        if isinstance(sal, int) or isinstance(sal, float):
            self.__salary  =sal
        else:
            raise ValueError("Salary cannot be string")



e = Employee("Ahmed",'Ahmed', 2034)
print(e.salary) # this function is treated as a property
# e.salary = 'iti'
e.salary = 3435
print(e.salary)
print(e.id)



