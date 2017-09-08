import pymysql
#wanted_table,wanted_str参数固定字符串,第三个可变
def getInfo(wanted_table,wanted_str,check_str,wanted_subscript_value,choice):
    db = pymysql.connect("localhost", "root", "", "new_schema")
    cursor1 = db.cursor()


        #修改数据表内容1）拿出具体某数据表内容
                #具体要什么内容，字符串不一样
                #修改某数据表的字符串就可以了
    # print("订票想要的数据")
    # wanted_table=input("什么数据表airplane")
    #     #用于精确确定的总字段名称
    # wanted_str=input("用于精确确定的总字段名称flight_ID")
    #     #待查询的字段名称
    # check_str=input("待查询的字段名称:客户自己输入的flight_ID")
    sql_select_flight = "select * from  %s where %s='%s'" %(wanted_table,wanted_str,check_str)
    if (choice == 'all airplane'):
        sql_select_flight = "select * from  airplane "
    if(choice=='order des airplane'):
        sql_select_flight="select * from airplane order by leftover desc"


    cursor1.execute(sql_select_flight)

    #取出想要数据，具体想要数据下标值不同，实际含义不同
    # wanted_subscript_value=input("取出想要数据，具体想要数据下标值不同，实际含义不同")

    rs=cursor1.fetchall()
    try:
        for row in rs:
            leftover = row[1]
            flight_ID = row[2]
            seat=row[3]
            if(choice=="show"or choice=='order des airplane' or choice=='all airplane'):
                print(row)

    except Exception as e:
        print(e)
        db.rollback()

    cursor1.close()
    db.close()
    return seat


# wanted_table = 'airplane'
# # 用于精确确定的总字段名称
# wanted_str = 'flight_ID'
# # 待查询的字段名称
# check_str = 'a1'
# wanted_subscript_value = 0
#
# #!!使用函数
# choice=''
# getInfo(wanted_table,wanted_str,check_str,wanted_subscript_value,choice)
        #原始数据展示

    #2）修改操作，具体想要的字段序号


    #3）再放回原处





#wanted_table,wanted_str参数固定字符串,第三个可变
def getInfo1(wanted_table,wanted_str,check_str,wanted_subscript_value,choice):
    db = pymysql.connect("localhost", "root", "", "new_schema")
    cursor1 = db.cursor()


        #修改数据表内容1）拿出具体某数据表内容
                #具体要什么内容，字符串不一样
                #修改某数据表的字符串就可以了
    # print("订票想要的数据")
    # wanted_table=input("什么数据表airplane")
    #     #用于精确确定的总字段名称
    # wanted_str=input("用于精确确定的总字段名称flight_ID")
    #     #待查询的字段名称
    # check_str=input("待查询的字段名称:客户自己输入的flight_ID")

    sql_select_flight = "select * from  %s where %s='%s'" %(wanted_table,wanted_str,check_str)
    if (choice == 'all airplane'):
        sql_select_flight = "select * from  airplane "

    cursor1.execute(sql_select_flight)

    #取出想要数据，具体想要数据下标值不同，实际含义不同
    # wanted_subscript_value=input("取出想要数据，具体想要数据下标值不同，实际含义不同")

    rs=cursor1.fetchall()
    try:
        for row in rs:
            leftover = row[1]
            flight_ID = row[2]
            seat=row[3]

    except Exception as e:
        print(e)
        db.rollback()

    cursor1.close()
    db.close()
    return seat


# wanted_table = 'airplane'
# # 用于精确确定的总字段名称
# wanted_str = 'flight_ID'
# # 待查询的字段名称
# check_str = 'a1'
# wanted_subscript_value = 0
#
# #!!使用函数
# choice=''
# getInfo(wanted_table,wanted_str,check_str,wanted_subscript_value,choice)
        #原始数据展示

    #2）修改操作，具体想要的字段序号


    #3）再放回原处
