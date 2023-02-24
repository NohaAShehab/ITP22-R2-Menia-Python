# import psycopg2
#
# dbuser= 'pythonmenair2'
# dbpassword = 'iti'
# dbname = 'meniacrud'
#
#
# try:
#     connection = psycopg2.connect(user=dbuser,password=dbpassword,
#                                   host='127.0.0.1',database=dbname, port='5432')
#
#     print(connection)
#     # conn = psycopg2.connect("dbname=meniacrud user=pythonmenair2 password=iti host=localhost")
#     # print(conn)
#     # create cursor  ---> connection to datbase
#     dbcursor  = connection.cursor()
#     print(dbcursor)  # will be used to perform operations
#     #### insert values in the table
#     query_insert = "insert into students (name, grade) values ('noha', 10)"
#     dbcursor.execute(query_insert)
#     connection.commit()
#     dbcursor.close()
#     connection.close()
#
# except (Exception, psycopg2.Error) as e:
#     print(e)

###########################################3


import psycopg2

dbuser= 'pythonmenair2'
dbpassword = 'iti'
dbname = 'meniacrud'


# try:
#     connection = psycopg2.connect(user=dbuser,password=dbpassword,
#                                   host='127.0.0.1',database=dbname, port='5432')
#     dbcursor  = connection.cursor()
#     name = input("please enter name: ")
#     grade = input("please enter grade ")  # do validation
#     query_insert = f"insert into students (name, grade) values ('{name}',{grade})"
#     dbcursor.execute(query_insert)
#     connection.commit()
#     dbcursor.close()
#     connection.close()
#
# except (Exception, psycopg2.Error) as e:
#     print(e)


##################################################################################
# try:
#     connection = psycopg2.connect(user=dbuser,password=dbpassword,
#                                   host='127.0.0.1',database=dbname, port='5432')
#     dbcursor  = connection.cursor()
#     name = input("please enter name: ")
#     grade = input("please enter grade ")  # do validation
#     query_insert = f"insert into students (name, grade) values ('{name}',{grade})"
#     dbcursor.execute(query_insert)
#     connection.commit()
#     dbcursor.close()
#     connection.close()
#
# except (Exception, psycopg2.Error) as e:
#     print(e)

#################### parameterized queries

#
# try:
#     connection = psycopg2.connect(user=dbuser,password=dbpassword,
#                                   host='127.0.0.1',database=dbname, port='5432')
#     dbcursor  = connection.cursor()
#     name = input("please enter name: ")
#     grade = input("please enter grade ")  # do validation
#     query_insert = """insert into students (name, grade) values (%s , %s)"""
#     record_info = (name, grade)
#     dbcursor.execute(query_insert,record_info)
#     connection.commit()
#     ### get rowcount
#     no_of_rows = dbcursor.rowcount
#     # no_of_rows = connection.rowcount
#     print(no_of_rows)
#     if no_of_rows:
#         print("---- data inserted successfully --- ")
#     dbcursor.close()
#     connection.close()
#
# except (Exception, psycopg2.Error) as e:
#     print(e)



try:
    connection = psycopg2.connect(user=dbuser,password=dbpassword,
                                  host='127.0.0.1',database=dbname, port='5432')
    connection.autocommit=1 ## enable autocommit.
    dbcursor  = connection.cursor()
    name = input("please enter name: ")
    grade = input("please enter grade ")  # do validation
    query_insert = """insert into students (name, grade) values (%s , %s)"""
    record_info = (name, grade)
    dbcursor.execute(query_insert,record_info)
    # connection.commit()  # mandatory step
    no_of_rows = dbcursor.rowcount
    print(no_of_rows)
    if no_of_rows:
        print("---- data inserted successfully --- ")
    dbcursor.close()
    connection.close()

except (Exception, psycopg2.Error) as e:
    print(e)





