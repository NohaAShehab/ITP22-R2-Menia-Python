
course = 'python'
def askforInt():
    while True:
        num = input("please enter number: ")
        if num.isdigit():
            return int(num)
        print("----------------- please enter valid number ----------")

