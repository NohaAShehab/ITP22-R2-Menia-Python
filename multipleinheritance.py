# class ParentA:
#     pass
#
#
# class ParentB:
#     def __init__(self):
#         print("-------Parent b called--------------")
#
# class Test(ParentA, ParentB):
#     pass
#
# t = Test()
# print(isinstance(t, ParentB))
# print(isinstance(t, ParentA))

#############################3
# class ParentA:
#     def __init__(self):
#         print("-------Parent A called--------------")
#         self.name ='Ahmed'
#
#     def eat(self):
#         print("--- I am parent 1 ")
#
# class ParentB:
#     def __init__(self):
#         print("-------Parent b called--------------")
#         self.name ='Ali'
#
#     def eat(self):
#         print("--- I am parent 2 ")
#
# class Test(ParentA, ParentB):
#     def __init__(self):
#         # super(Test, self).__init__()
#         ParentB.__init__(self)
#         super().__init__()  # call parent constructor --->
#         print("---- Test constructor called -----")
#
# t = Test()
# t.eat()
####################


class ParentA:
    def __init__(self):
        print("-------Parent A called--------------")
        self.name ='Ahmed'

    def eat(self):
        print("--- I am parent 1 ")

class ParentB:
    def __init__(self):
        print("-------Parent b called--------------")
        self.name ='Ali'

    def eat(self):
        print("--- I am parent 2 ")

class Test(ParentA, ParentB):
    def __init__(self):
        # super(Test, self).__init__()
        ParentB.__init__(self)
        super().__init__()  # call parent constructor --->
        print("---- Test constructor called -----")

t = Test()
t.eat()























