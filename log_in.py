import fileinput
import pymysql
# def log_in():
#     # with fileinput.input('test.txt') as f:
#     #     for line in f:
#     #         name=line
#     #         password=line
#     db=pymysql.connect("localhost","root","","new_schema")
#     cursor=db.cursor()
#
#     name=input("input user_enter_name")
#     password=input("input password")
#     # name='Zheng'
#     # password='z1'
#     sql_select="select * from user_info where user_name='%s'"%name
#     cursor.execute(sql_select)
#     rs=cursor.fetchall()
#     for row in rs:
#         user_name=row[1]
#         user_password=row[2]
#
#
#     count=0
#     while count<3:
#         if(user_name!=name and user_password!=password):
#             count+=1
#             print("error pass ")
#
#         else:
#             print("success enter")
#             break
#     cursor.close()
#     db.close()
#     return user_name

import fileinput
import pymysql
def log_in():
    # with fileinput.input('test.txt') as f:
    #
    #         name=f[0]
    #         print(name)
    #         password=f[1]
    #         print(password)
    db=pymysql.connect("localhost","root","","new_schema")
    cursor=db.cursor()

    # name=input("input user_enter_name")
    # password=input("input password")

    name='Zheng'
    password='z1'
    sql_select="select * from user_info where user_name='%s'"%name
    cursor.execute(sql_select)
    rs=cursor.fetchall()
    for row in rs:
        user_name=row[1]
        user_password=row[2]


    count=0
    while count<3:
        if(user_name!=name and user_password!=password):
            count+=1
            print("error pass ")

        else:
            print("success enter")
            break
    cursor.close()
    db.close()
    return user_name
# log_in()