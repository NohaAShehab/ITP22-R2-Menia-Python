# #### logical error --->
# def sumnums(num1,num2):
#     return num1 * num2
#
# x = sumnums(2,20)
# print(x)
## debug
##test cases -unit test-

################ Runtime --- > Exception #############################
# unexpected event caused the application to stop
# print(name)
print("----------------------------------")
# print(6/0)
print("---------Errors and Exceptions ---------------")
# num = int(input("please enter number: "))

# ############### Exception handling ########################
# try:
#     print(name)
#
# except:
#     # handle the exception here
#     print("---- variable not found -------")
#
#
# print("---- Nice to meet you ----------------")
######################################
# try:
#     print(name)
#
# except:
#     # handle the exception here
#     print("---- variable not found -------")
#     name = None
#
#
# print("---- Nice to meet you ----------------")
###########################################
from iti import askforInt

# num1 = askforInt()
# num2 = askforInt()
# try:
#     division =num1/num2
# except Exception as e :
#     print(f"------------ problem happened--{e}------")
#     division = None
#
# print(division)
################################################
# try:
#     num1 = int(input('please enter num1: '))
#     num2 = int(input('please enter num2: '))
#     res = num1/num2
# except ValueError as ve:
#     print(ve)
#     num1 = 1
#     num2 =1
#     print("------- problem happend with the input parameters ")
#     res = num1/num2
# except ZeroDivisionError as ze:
#     print(ze)
#     res = 0
# except Exception as e:
#     print(e)
#
#
# print(res)


###################################################
# try:
#     num1 = int(input('please enter num1: '))
#     num2 = int(input('please enter num2: '))
# except Exception as e:
#     print(e)
# else:
#     res = num1 + num2
#     print(res)
################## finally block
try:
    num1 = int(input('please enter num1: '))
    num2 = int(input('please enter num2: '))
except Exception as e:
    print(e)
else:
    res = num2 + num1
    print(res)
finally:
    print("==== this block will be executed always ===")
























































