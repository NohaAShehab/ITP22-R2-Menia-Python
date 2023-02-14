
# any variable defined in the python script ----> global variable
## can be accessed anywhere in the script
# course = 'python'  ## defined variable ?
#
# print(course)
#
# course = 'OOP with Python'
#
#
# ##### access global variable from inside a function
#
# def printcourseinfo():
#     print(f"====from inside the function course = {course}")
#
# printcourseinfo()

########################################################################

# course = 'Python'
#
# def modifycourse():
#     # when you define variable inside the function
#     ## the variable is created scope --->  local scope
#     course = 'Django'   # local variable ### can be accessed only in the function
#     print(f"from the function course = {course}")
#     return course
#
# print(f'course = {course}')
# m= modifycourse()
# print(f'course = {course}')

################### function modify global variable
# course = 'python'
#
# def modifycourse():
#     global course
#     course = 'django'
#     print(f"course {course} in the function")
#
# print(course)
# modifycourse()
# print(course)

################################################

res = 0
def modifyresult():
    global  res
    res =10

modifyresult()

##########################3
summ= 0
def modifysumm():
    return 10

summ = modifysumm()


























