
#
# class Employee:
#     nationality = 'Egyptian'
#     count = 0
#
#     def __init__(self, name, email, salary):
#         self.name = name
#         self.email = email
#         self.salary = salary
#         Employee.count += 1
#
#     def speak(self):  # self --> represent object /caller instance
#         print(f"my name is {self.name}, you contact me at {self.email}")
#
#     def greeting(self, message=''):
#         print(f"My name is {self.name}, {message}.")
#
#     @classmethod
#     def create_defaultobject(cls):
#         return cls("", '', 0)
#
#
# #### calculate net salary ?
# e = Employee('Ahmed', 'ahmed@gmail.com',20000)
# print(e.salary)
#
# def cal_net_sal(salary):
#     return salary*.86
#
# print(cal_net_sal(e.salary))
# print(cal_net_sal(100000))
###########################################

class Employee:
    nationality = 'Egyptian'
    count = 0

    def __init__(self, name, email, salary):
        self.name = name
        self.email = email
        self.salary = salary
        Employee.count += 1

    def speak(self):  # self --> represent object /caller instance
        print(f"my name is {self.name}, you contact me at {self.email}")

    def greeting(self, message=''):
        print(f"My name is {self.name}, {message}.")

    @classmethod
    def create_defaultobject(cls):
        return cls("", '', 0)

    @staticmethod
    def cal_net_sal(salary):
        return salary * .86

    @staticmethod
    def test():
        print("------------")

    #
    # def get_net_sal(salary):  #  salary ----> self
    #     print(salary)
    #     # return salary* .89

    # @classmethod
    # def get_net_sal(salary):  #  salary ----> cls
    #     print(salary)
    #     # return salary* .89
    @staticmethod

    def get_net_sal(salary):  #  salary ----> self
        print(salary)
        # return salary* .89


#### calculate net salary ?
e = Employee('Ahmed', 'ahmed@gmail.com',20000)
print(e.salary)
## instance method ---> You to have an instance from the class
#
# print(Employee.cal_net_sal(e.salary))
# print(Employee.cal_net_sal(9869748976))
#

e.get_net_sal(344)





