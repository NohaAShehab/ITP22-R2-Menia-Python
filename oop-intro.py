### describe data using labels -keywords-

# info =['Noha', 30 , 'ITI'] ##

# info ={"name":"Noha", "age":30, "work":"ITI"}
# print(info)


# emp1 = {"name": "Ahmed", "salary": 30000, "Company": 'Microsoft'}
# emp2 = {"name": "Ali", "salary": 40000, "Company": 'Amazon'}
# emp3 = {"name": "Mohamed", "salary": 30000, "Company": 'Microsoft', 'email': "test@gmail.com"}

# define general structure that represent real world object ---> Classes
## class ---> blueprint or structure for certain element --> represent properties , + functionality

# 1- to define class  ---> define your own datatype ## classes user defined datatype

# class Employee:
#     pass
# # object from class
# emp1 = Employee()    # generate new object ?
# # ## loosely dynamically typed lang.
# emp1.firstname = 'Noha'
#
# emp2 = Employee()
# emp2.name = 'Ali'
# emp2.email = 'ali@gmail.com'


############################3
### constructor function  --> this function will be used while creating object

# class Employee:
#     def __init__(self):
#         print(f"---- the object is being created  {self}")
#
#
# e = Employee()
# print(e)
# e.name ='Ahmed'
# emp2 =Employee()
#####################################

# class Employee:
#     def __init__(self):
#         print(f"---- the object is being created  {self}")
#         self.name = 'Ahmed'
#         self.email =  'ahmed@gmail.com'
#         self.salary = 2000
#
#
# e = Employee()
# emp2 = Employee()

##################

# class Employee:
#     def __init__(self, name, email , salary):
#         print(f"---- the object is being created  {self}")
#         ## object properties
#         self.name = name
#         self.email =  email
#         self.salary = salary
#
#
# e = Employee('Ahmed', 'ahmed@gmail.com',445)
# print(e.name)
# e.name = 'AhmedAli'
# emp2 = Employee('Ali', 'ali@gmail.com', 234)

##################################################

# class Employee:
#     def __init__(self, name='', email='' , salary=0):
#         print(f"---- the object is being created  {self}")
#         ### name, email ,salary ---> instance variables --> values --> depends the instance/object
#         ## object properties
#         self.name = name
#         self.email =  email
#         self.salary = salary
#
#
# e = Employee('Ahmed', 'ahmed@gmail.com',445)
# print(e.name)
# e.name = 'AhmedAli'
# emp2 = Employee()
# emp2.city='Cairo'

########################### instance methods

# class Employee:
#     def __init__(self, name='', email='' , salary=0):
#         print(f"---- the object is being created  {self}")
#         ### name, email ,salary ---> instance variables --> values --> depends the instance/object
#         ## object properties
#         self.name = name
#         self.email =  email
#         self.salary = salary
#
#     # instance methods
#     def speak(self):  # self --> represent object /caller instance
#         print(f"my name is {self.name}, you contact me at {self.email}")
#
#     def greeting(self, message=''):
#         print(f"My name is {self.name}, {message}.")
#
# emp2 = Employee("Noha", 'noha@gmail.com', 1000)
# emp2.speak()
# emp2.name = 'NohaShehab'
# emp2.speak()
# emp2.greeting('Nice to meet you.,...')
########################################################################

# class Employee:
#     ## class variables => variables ---> depend on the class itself not the instance
#     nationality ='Egyptian'
#
#     def __init__(self, name='', email='' , salary=0):
#         self.name = name
#         self.email =  email
#         self.salary = salary
#
#     def speak(self):  # self --> represent object /caller instance
#         print(f"my name is {self.name}, you contact me at {self.email}")
#
#     def greeting(self, message=''):
#         print(f"My name is {self.name}, {message}.")

# emp2 = Employee("Noha", 'noha@gmail.com', 1000)
# emp2.company = 'Oracle'
# emp3 = Employee("Noha", 'noha@gmail.com', 1000)
# ### you can access class variable ---> using class it self
# print(Employee.nationality)
# emp2.name ='Abdallah'
# Employee.nationality = 'Test'
###################### class method
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

    ### class methods ---> define behaviour for the class

    # @classmethod
    # def get_emp_count(cls):  # first argument in the method --> represent current class
    #     print(cls)
    #     print(cls.count)
    ## class method ---> object factory
    @classmethod
    def create_defaultobject(cls):
        return cls("", '', 0)

    @classmethod
    def add_employee(cls, emp1 , emp2):
        if isinstance(emp1, cls) and isinstance(emp2, cls):
            name = emp1.name + emp2.name
            email = emp1.email
            salary = emp1.salary + emp2.salary
            return Employee(name, email, salary)

    # def __add__(self, emp1):
    #     self.name +=emp1.name

e = Employee("Ahmed", '', 10000)
e2 = Employee("Ali", '', 20000)
print(e2.count)

e.__add__(e2)
print(e.name)

# e3 = Employee.create_defaultobject()
# e4 = Employee.add_employee(e, e2)
# print(e4.name)
# print(e4.salary)


########
l1 = [444]
l2 = [45,44,6]

l3= l1 + l2

################################








