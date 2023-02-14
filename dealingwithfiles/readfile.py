
## 1- open the file --? read r, writing  w, append a , rb , wb
##fileobj=open(filename :str, mode) ---> IOStream.TextIOWrapper
## 2- do operation
## fileobj.read() ====> string
## fileobj.write('message')
## 3- close file
## fileobj.close()

try:
    fileobject = open("students.txt", 'r')
except Exception as e:
    print(e)
else:
    print(fileobject)
    # data  = fileobject.read()  # read file content into one String from the begining
    # # of the file  .

    # data =  fileobject.read(10)  # read first 10 bytes from the beginning of the file
    # print(data)

    # fileobject.seek(10)
    # data = fileobject.read(5)
    # print(data)

    # data = fileobject.read()
    # print(data)  # read whole the file
    # fileobject.seek(0)  # seek byte number
    # mm = fileobject.read()
    # print(mm)

    # dd = fileobject.read(10)
    # print(dd)
    # fileobject.seek(0) # skip chars from the begining of the file
    # print("-------------------------------------")
    # mm=fileobject.read(5)
    # print(mm)

    #### read file line by line
    # lines  = fileobject.readlines()  # read file content into a list
    # print(lines)
    ######
    # line = fileobject.readline()  # read one line from the file,
    # print(line)

    #################################
    for l in fileobject:
        print(f"line = {l}")


    fileobject.close()



#######################
import  os

os.system('ls -l')
print("-----------------------------")
os.system("awk -F: '{print $2}' students.txt ")

# ##################################################
