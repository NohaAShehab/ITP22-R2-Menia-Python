

name = 'Noha' ### index start from 0
# print(name[3])

# calculate len of the string ?

# print(len(name))

work = 'information technology Institute'
# print(work[2:8])  # substring from start to end-1
# count no of occurneces of char in the string.
# print(work.count('i'))

# get index of char in the string
# print(work.index('i'))  # get the index of the first occurence of the string.

### operations
### string concatenation  ===> between strings only
# firstname= 'Noha'
# midname = 'Abdelhady'
# lastname = 'Shehab'

# fullname = firstname + midname + lastname
# string interpolation
# fullname = firstname + midname + midname + lastname
# fullname = firstname + midname *2  + lastname
# print(fullname)

###############################################
## string is immutable datatype ? ---> cannot be changed

## replace --->
# name = 'noha a a a a a a' # a --> @
# name =name.replace('a', '@')  # return new string
# print(name)

# name =name.replace('a', '@', 2)  # return new string
# print(name)

########### string formatting
#
# temp= 'My name is {0}  I works at {1}'
# print(temp)
# format
# print(temp.format('Noha', 'iti'))  # new string
# print(temp.format('Ahmed','IBM'))

# print(temp.format('IBM', 'Ahmed'))

#########################################################


# temp= 'My name is {username}  I works at {userwork}'
# print(temp.format(username='Noha', userwork='ITI'))
# print(temp.format( userwork='ITI', username='Noha'))
####################### f-format string
# name = 'Noha'
# work = 'ITI'
# year = 2023
# mystring = f"My name is {name}, I works at {work} {year}"
# print(mystring)

#### accept input from the user
# userinput =input("please enter name : ")  # string

# age = input("please enter age  ") # string
# if age.isdigit():
#     age = int(age)
# else:
#     print("-------- not valid age -------------")
# print(userinput.isalpha())  # check string consists only from alphas
# print(userinput.isspace())  # check if the string ---> consists only from spaces

################################
# print(userinput.capitalize())
#
# print(userinput.upper())  ###
# print(userinput.lower())
# print(userinput.isupper())   # islower()
#########################################
########### strip string #####################

# message = '            my name is noha                 '
# print(len(message))
## strip
# print(message.strip())  # return new string ---> strip remove spaces from the begining and
# the end of the string
# print(message.lstrip())
# print(message.rstrip())

##################################

# message = '            my name is noha                 .'
# print(message.strip())

# message = '            my name is noha                 .'
# print(message.strip('. '))  # remove any char specified in the fun

#################### loops , range ===

#loop over string --->
## string  ---> iterable
# message = 'I love Python.'
# for c in message:
#     print(f"c= {c}#")

###### looping
### while
# while True:
#     name = input("please enter name ")
#     if name.isalpha():
#         break


##########
message = 'I love Python.'
# print(len(message))
# for c in message:
#     print(f"c= {c}#")


### generate number in python --->sequence of numbers
# numrange = range(10)
# print(numrange)  # ---> iterable object ---> for loop
# for num in numrange:
#     print(num)

# numrange = range(1,10)
# print(numrange)  # ---> iterable object ---> for loop
# for num in numrange:
#     print(num)



numrange = range(1,10, 2)
print(numrange)  # ---> iterable object ---> for loop
for num in numrange:
    print(num)


### with string in operator

print('o' in 'noha')


mystr = 'I works at iti , I lives in iti '


# noha ===> nh 

























