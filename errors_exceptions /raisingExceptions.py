
from iti import  askforInt

def divnums():
    num1 = askforInt()
    num2 = askforInt()
    if num2==0:
        raise ZeroDivisionError("--- invalid operation division by zero ---")
    print("----------- Thank you for entering num1 , num2 ")
    print(f"num1 = {num1}, num2 ={num2}")
    res = num1 / num2
    print(res)


divnums()