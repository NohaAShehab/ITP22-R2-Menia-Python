##################### functions ######################
# num1= input("please enter num1 : ")
# if num1.isdigit():
#     num1 = int(num1)
#
# num2= input("please enter num2 : ")
# if num2.isdigit():
#     num2 = int(num2)


# def functionname():
#     pass
#
# functionname()


############################

# def functionname():
#     print("----- Hello World --------------")
#
# functionname()
# functionname()
# functionname()
# x = functionname()
# print(x)  # None ??? falsy values

###########################

# def saywelcome():
#     print("welcome")
#     return
#
# m = saywelcome()
# print(m)

#####################
# def getfullname(firstname, lastname):
#     fullname = f"{firstname} {lastname}"
#     print(fullname)
#     return fullname
#
# f=getfullname("Ahmed", "Ali")
# print(f)
#
# m = getfullname(3,5)
# print(m)
#################################################

# def getfullname(firstname: str, lastname: str) -> object:
#     fullname = f"{firstname} {lastname}"
#     print(fullname)
#     return fullname
# getfullname('Ahmed', 'ali')
# getfullname(5,6)

###########################

# def getfullname(firstname: str, lastname: str) -> str:
#     if isinstance(firstname, str) and isinstance(lastname, str):
#         fullname = f"{firstname} {lastname}"
#         print(fullname)
#         return fullname
#
# # m = getfullname('Noha', 'Shehab')
# # print(m)
# m = getfullname(5, 'Shehab')
# print(m)


### function with default arguments

# def sumnums(num1=5, num2=3):
#     print(f"{num1}, {num2}")
#     return num1 + num2
#
# sumnums(4)
# sumnums()
#
# def sumnums(num2, num1=5):
#     print(f"{num1}, {num2}")
#     return num1 + num2
#
# sumnums(4)
###########################################
#### functions with variable number of arguments
#
# print('Ahmed')
# print(3,5,6,7)

# def getmulnums(*nums):  # unknown number of arguments
#     print(nums)
#
#
# getmulnums(3, 5, 6)
# getmulnums(35, 66, 323, 234, 23)

################# functions

def introduceyourself(**info):  # function accepts unknow number of keyword arguments.
    print(info)
    for k, v in info.items():
        print(f"{k},{v} ")

    print("---------------------------")


introduceyourself(name='noha', work='iti', age=30)
introduceyourself(fname='Dina', lname='Rabea')
introduceyourself()

['Ahmed','apple', 'iti']

# random in python

'-pp--'







