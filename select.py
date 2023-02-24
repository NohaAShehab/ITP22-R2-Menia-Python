import psycopg2

from connection import connectTodatabase

connobj = connectTodatabase()

try:
    query = """select * from students; """
    dbcursor = connobj.cursor()
    res=dbcursor.execute(query)
    # print(res)
    # ## use cursor to fetch the data
    # records = dbcursor.fetchall()  # fetch all data from the database in a list of tuples
    # # each tuple represent record in the database
    # print(records)
    # print(type(records))
    # onerecord = dbcursor.fetchone()
    # print(onerecord)

    for rcrd in dbcursor:
        print(rcrd)

    # insert into fff (,) value (), (), ()

    # print(dbcursor.fetchmany(3))
    dbcursor.scroll(0, mode='absolute')  # reset the cursor

    for rcrd in dbcursor:
        print(rcrd)


except (Exception, psycopg2.Error) as e :
    print(e)



