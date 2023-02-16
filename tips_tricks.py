
#### swap in python
# num1= 10
# num2 = 'iti'

# temp = num1
# num1 = num2
# num2 =temp
#
# # print(num1, num2)
# #################3
#
# num1= 10
# num2 = 'iti'
#
# num1, num2 = num2, num1
#
# print(num1, num2)
#
#
# # num1 =10
# # num1 = 20
# # num1 = 43
# # num1 = 10
# # print(num1==10 and num1==20 and num1==30)
# #####################3
# # sequence unpacking
# myl = [43,656,57,True,'jksfh', 34]
# # a,b,c,d =myl
#
# # a,b,*c = myl
# a, *b, c = myl
#
#
#
# # with open("mycv.txt", 'w') as fileobj:
# #     fileobj.write("fkdjf")
#
#
# #### list comprehension
#
# #
# l = list(range(1,11, 1))
# print(l)
#
# myl = [ x*x  for x in range(1,11)]
# print(myl)
#
# myl = [ x*x  for x in range(2,11,2) ]
# print(myl)
#
# # myl = [ x*x  for x in range(2,11) if x%2==0]
# # print(myl)
#
# myl = [ x*x  for x in range(2,11) if x%2==0 ]
# print(myl)
#
# l= [x*2 if x !=4 else 44 for x in range(18)]
# print(l)
#
# ### tinary operator
# name = 'noha'
# print(name if name=='Ahmed' else 'not found')
#
# mm = ["4","9", "0", 'iti', "343.45", "True", 434,566,34, False]
#
# print(all(mm))  # False # if all members in the iterable represent True ---> True
# print(any(mm))  # True ---> return True if there is only one Truly value in the iterable

##########################################################################3

def addfour(num):
    return num +4

# print(addfour(33))
# print(addfour(439048))
name = 'noha'

print(globals())  # print all global variable in the script

#### function ---> call it only ?
# def myfun():
#     print("---- calling my fun")
#     return addfour(10)
#
# x = myfun()
### return with another function ---> not calling the function
#
# def myfun():
#     print("--- calling my fun")
#     return lambda x : x +4
# res = myfun()  # lambda expression ----> anonymous function
#
# mm= myfun()(200)
# print(mm)
# print(res(10))
# res = myfun()
# # print(res)
# x= res(34)


ss = lambda x : x+ 10
print(ss(10))

#
# def myfun():
#     y = 10
#     print("--- calling my fun")
#     return lambda x : x +y
#
# m = myfun()
# print(m)
# print(m(34))


l = [10, 40, 34, 45]


# #
# myl = map(lambda x:x*4, l)
# # print(myl)  # map object  # iterable ?
# # ll = []
# for m in myl:
#     print(m)
#     ll.append(m)


# mm  =map(lambda x:x*4,[4,5,6,7])  # map object
# print(list(mm))
##############################
# ss = filter(lambda  x : x%2==0, [3,5,6,7,54,4,32,20,32])
# print(ss)
# ss = list(ss)
# print(ss)

# ss = [3,5,6,7,54,4,32,20,32]
#
# ss = filter(lambda  x : x%2==0, [3,5,6,7,54,4,32,20,32])
# print(ss)
# ss = list(ss)
# print(ss)

################# iterators and generators

# ll = ['test', 'abc', 'iti' , False,33, 33.44]
# myiter = iter(ll)
# print(myiter)
# print(next(myiter))
# ###########################3
# print(next(myiter))
# ########################
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))


###################### Generator #########################
### generate set of values

# mm = list(range(1, 1000000))


def generatenum():
    for i in range(10000000):
        yield i


### generate value once needed

mygen = generatenum()
print(next(mygen))
print(next(mygen))
print(next(mygen))


###################3

def myfuction():
    trac = 'python'
    intake =43
    branch = 'Menia'
    print(locals())

myfuction()

# class Queue:
#     instance = {"myq":[45,45]}
#
