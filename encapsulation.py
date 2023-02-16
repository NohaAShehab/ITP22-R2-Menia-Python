# class Engineer:
#     count= 0
#     def __init__(self,name=''):
#         self.name= name
#         Engineer.count +=1
#
#     def printinfo(self):
#         print(f"{self.name}")
#
#
# print(Engineer.count)

### limit accessiblity ---> access modifiers
## public  --> class memeber  ---> can be accessed anywhere (from outside --> using member )
## private ---> can be accessed in the class only
## protected ---> can be accessed only in the class ---> derived class
############## No access modifiers ################
## rules  ---> in naming identifers
## [a-z] -----> public
## _[a-z] ====> protected
## __[a-z] ====> private

#### access modifiers ---> limit accessibility of the class members

# class Employee:
#     def __init__(self,name, email, salary):
#         self.name = name
#         self._email= email  # protected
#         self.__salary = salary
#
#
#     def printEmpInfo(self):
#         print(f"""my name is {self.name},
#         My email is {self._email}
#         my salary is {self.__salary}""")
#
#     def _protected(self):
#         print("protected")
#
#     def __private(self):
#         print("--- this is the private method ----")
#
# e= Employee("Ahmed", "Ahmed@gmail.com", 40000)
# print(e.name)
# e.name = 'Noha'  # access class member  --> property _name using the instance outside the class .
# e.printEmpInfo()
# ### protected ---> access member only in the class ---> or in the drived class
# print(e._email) # don't do this ethically
# e._email = 'updated'
# # print(e.__salary) # 'Employee' object has no attribute '__salary'
# ### it is not recommend to do something like this
# # e.__salary = 2893  # this property is added to the object in the run time
# # print(e.__salary)  # you can access it in the run time
# ############## It's not recommended to do something like this ?  # clean code
# # print(e._Employee__salary)  # modify private member using scope binding
# # e._Employee__salary = 9383244
#
# e._protected()
# # e.__private()
# # e._Employee__private()


########################