


# def myfunction():
#     track ='full stack using python'  # local variable  can be accessed anywhere in the function
#     def innerfun():
#         print("===== calling the inner function =====")
#         print(f'== from the inner function track ={track}.')
#
#     print(f"track = {track}")
#     innerfun()
#
#
#
# myfunction()

# def myfunction():
#     track ='fullstack using python'  # local variable  can be accessed anywhere in the function
#     def modifytrack():
#         print("===== calling the inner function =====")
#         track = 'Backend Python'  # create new local variable for the modify track function
#         print(f'== from the inner function track ={track}.')
#
#     print(f"track = {track}")
#     modifytrack()
#     print(f"track = {track}")
#
#
#
# myfunction()



# def myfunction():
#     track ='fullstack using python'  # local variable  can be accessed anywhere in the function
#     def modifytrack():
#         print("===== calling the inner function =====")
#         nonlocal track
#         track = 'Backend Python'  # create new local variable for the modify track function
#         print(f'== from the inner function track ={track}.')
#
#     print(f"track = {track}")
#     modifytrack()
#     print(f"track = {track}")
#
#
#
# myfunction()
# print("===================")
#




# name = 'Ahmed'
#
# def outerA():
#     def innerB():
#         def innerC():
#             global name
#             name = 'Ali'
#         innerC()
#     innerB()
#
# print(name)
# outerA()
# print(name)




# def outerA():
#     name = 'Ahmed'
#     def innerB():
#         def innerC():
#             nonlocal name
#             name = 'Ali'
#         innerC()
#     innerB()
#
#     print(name)
#
# outerA()
############################################
name = '#######################'
print("-------------- in the local scoping module ----------------")
def outerA():
    name = 'Ahmed'
    def innerB():
        def innerC():
            global name
            name = 'Ali'
        innerC()
    innerB()

    print(name)
























