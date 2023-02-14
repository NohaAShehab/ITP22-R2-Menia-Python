
#
# try:
#     fileobj = open("mycv.txt", 'r+')  # reading and writing
# except Exception as e:
#     print(e)
#
# else:
#     print(fileobj)
#     data = fileobj.read()
#     print(data)
#     fileobj.write('Ahmed')
#     fileobj.seek(200)
#     fileobj.write('-3059-05935----')
#     # fileobj.seek(200)
#     fileobj.close()

######################3


try:
    fileobj = open("test.txt", 'w+')  # reading and writing
except Exception as e:
    print(e)

else:
    fileobj.write('test')
    print(fileobj)
    fileobj.seek(0)
    data = fileobj.read()
    print(f"data = {data}")

    fileobj.close()





