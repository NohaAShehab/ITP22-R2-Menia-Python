### divide code to modules , functions

## id ---> user

# import  time
# print(round(time.time()))

# {"id": 2, }

### json.loads()
### json.dumps()
##########################################
# .txt
import time

t= round(time.time())
name= input("enter name: ")
age = input("enter age : ")

data = f"{t}:{name}:{age}\n"
print(data)

myfile = open('users.txt', 'a')
myfile.write(data)
myfile.close()

#### split


# choice = input("please enter c for create , l for list ll")
# if choice=='c':
#     project_title = ''

