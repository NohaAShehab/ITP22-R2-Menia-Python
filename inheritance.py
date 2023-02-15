

# class Human:
#     pass
#
# class Employee(Human):
#     pass
#
#
# e = Employee()
# print(isinstance(e, Employee))
# print(isinstance(e,Human))  # inheritance is a relationship

##################################
#
# class Human:
#     def __init__(self):
#         print("---- Human object created ------------")
#
# class Employee(Human):
#     pass
#
#
# e = Employee()
# print(isinstance(e, Employee))
# print(isinstance(e,Human))  # inheritance is a relationship
############################

# class Human:
#     def __init__(self,name):
#         print("---- Human object created ------------")
#         self.name = name
#
# class Employee(Human):
#     pass
#
#
# e = Employee('Ali')
# print(isinstance(e, Employee))
# print(isinstance(e,Human))  # inheritance is a relationship

############################
# class Human:
#     def __init__(self,name):
#         print("---- Human object created ------------")
#         self.name = name
#
# class Employee(Human):
#     def __init__(self,email):
#         self.email = email
#
# e = Employee('Ali')
# print(isinstance(e, Employee))
# print(isinstance(e,Human))  # inheritance is a relationship

#############################

# class Human:
#     count = 0
#     def __init__(self,name):
#         print("---- Human object created ------------")
#         self.name = name
#         Human.count +=1
#
#     def speak(self):
#         print(f"my name is {self.name}")
#
#     @classmethod
#     def humanmethod(cls):
#         print("I am human")
#
# class Employee(Human):
#     def __init__(self,name, email):
#         super().__init__(name)  # explicitly call the parent constructor
#         self.email = email
#
# e = Employee('Ali', 'ali@gmail.com')
# print(isinstance(e, Employee))
# print(isinstance(e,Human))  # inheritance is a relation
# e.speak()
# Employee.humanmethod()

############################# polymorphism
class Human:
    count = 0
    def __init__(self,name):
        print("---- Human object created ------------")
        self.name = name
        Human.count +=1

    def speak(self):
        print(f"my name is {self.name}")

    @classmethod
    def humanmethod(cls):
        print("I am human")

class Employee(Human):
    def __init__(self,name, email):
        super().__init__(name)  # explicitly call the parent constructor
        self.email = email

    def speak(self):
        # super().speak()
        print(f'My name is {self.name}, You contact me at {self.email}')

    def speak(self, message:str):
        pass


e = Employee('Ali', 'ali@gmail.com')
print(isinstance(e, Employee))
print(isinstance(e,Human))  # inheritance is a relation
e.speak()
# Employee.humanmethod()






































