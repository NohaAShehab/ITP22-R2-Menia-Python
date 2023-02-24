# import psycopg2
# from connection import  connectTodatabase
#
# connection_obj = connectTodatabase()
#
# if connection_obj:
#     print("--- connected successfully")
#
#     studentname = input("please enter student name: ")
#     grade = input("please enter student grade: ")
#     query = """insert into students (name, grade) values (%s, %s)"""
#     try:
#         dbcursor = connection_obj.cursor()
#         inserted_data = (studentname, grade)
#         dbcursor.execute(query, inserted_data)
#
#         commit_ok = input("Data are ready to be inserted, type y for save: ")
#         if commit_ok=='y':
#             connection_obj.commit()
#             print("---- data inserted successfully")
#         else:
#             connection_obj.rollback()
#
#         dbcursor.close()
#         connection_obj.close()
#     except (Exception, psycopg2.Error) as e:
#         print(e)
#
# else:
#     print("--- connection filed")


import psycopg2
from connection import  connectTodatabase

connection_obj = connectTodatabase()

if connection_obj:
    print("--- connected successfully")

    studentname = input("please enter student name: ")
    grade = input("please enter student grade: ")
    query = """insert into students (name, grade) values (%s, %s)"""
    try:
        dbcursor = connection_obj.cursor()
        inserted_data = (studentname, grade)
        dbcursor.execute(query, inserted_data)

        commit_ok = input("Data are ready to be inserted, type y for save: ")
        if commit_ok=='y':
            connection_obj.commit()  #  connection.autocommit=1
            print("---- data inserted successfully")
        else:
            connection_obj.rollback()

        dbcursor.close()
        connection_obj.close()
    except (Exception, psycopg2.Error) as e:
        print(e)

else:
    print("--- connection filed")
