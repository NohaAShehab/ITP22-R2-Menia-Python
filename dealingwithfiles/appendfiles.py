
### when you open file with append mode ---> if the file
## doesn't exist -- > python will try to create it ?
## if file exists ---> python open file for writing starting from
# the end of the file -keep old content -
try:
    fileobj = open("mycv.txt", 'a')
except Exception as e:
    print(e)
else:
    print(fileobj)
    fileobj.write('My name is Noha\n')
    fileobj.write("I works at ITI\n")
    fileobj.seek(10)
    fileobj.writelines(['abc', 'test', 'bla bla bla'])
    # fileobj.seek(50)
    # fileobj.write('I love python\n')

    fileobj.close()

