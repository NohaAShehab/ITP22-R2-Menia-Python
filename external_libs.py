# import  os
# print(os.getcwd())
# # print(os.system('touch myfile.json'))
# os.mkdir('testtt')

import math
# print(math.pi)
# print(math.ceil(34.33))
#
# import os
#
# os.system(' touch test.csv')

#####################################
import  re
regexx = r"^[A-Za-z]+[-_$.A-Za-z]*@[A-Za-z]*\.[A-Za-z]+$"

email = input("please enter email: ")

# if re.match(regexx, email):  # retrurn with match object --> if part of the string
#     # statisfy the pattern
#     print("---email valid")
# else:
#     print("--- email not valid ")


if re.fullmatch(regexx, email):  # retrurn with match object --> if part of the string
    # statisfy the pattern
    print("---email valid")
else:
    print("--- email not valid ")




