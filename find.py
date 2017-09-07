import pymysql
import getInfoFromMySQL
def find():#按照输入的特定功能查询，
    print("请输入查询信息：1.按航班 2.按剩余人数 3.按起始地点")
    # _input=input()
    _input=1
    db = pymysql.connect("localhost", "root", "", "new_schema")
    cursor = db.cursor()
    try:
            if(_input==1):
                # _input=input()
                _input='A1'
                print("输入航班号: %s"%_input)
                sql_select="select * from airplane where flight_ID='%s'"%_input
            if(_input==2):
                print("查询剩余航班")
                sql_select="select * from airplane where leftover>0"
            if(_input==3):
                print("输入起始位置")
                _input=input()
                sql_select="select * from airplane where start_position='%s'"%_input
            cursor.execute(sql_select)
            rs = cursor.fetchall()

            #航班信息展示
            print("member|| leftover|| flight_ID|| start_position || destination || leaving time||arriving time")
            for row in rs:
                leftover=row[1]
                flight_ID=row[2]
                print("您的航班信息：%s"%row,"\n")

    except Exception as e:
                print(e)
                db.rollback()


# find()