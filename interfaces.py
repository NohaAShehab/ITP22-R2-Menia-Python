### no interface keyword in python

## interfaces ---> multiple inheritance
### define general strucure -- without any implementation
import zope.interface
from zope.interface import Interface, implementer
class ShapeInterface(Interface):
    def calarea(self):
        pass

    def calcir(self):
        pass


#
# @implementer(ShapeInterface)
# class Square:
#     def calcir(self, dim):
#         return dim*4
#
#     def calarea(self, dim):
#         return dim**2
#
#
# s = Square()
# print(s.calcir(3))
#
# # print(issubclass(Square, ShapeInterface))
# print(list(zope.interface.providedBy(s)))
#
# # print(type(s))