import pymysql
import fileinput
import getInfoFromMySQL




def cancel_ticket(user_name):
    judge=1
    db = pymysql.connect("localhost", "root", "", "new_schema")
    cursor1 = db.cursor()
    try:

        # 2、取消订票
        print("cancel ticket? please input 1 or 0")
        # cancel_ticket=input()
        cancel_ticket = 1
        cancel_ticket = int(cancel_ticket)

        seat = getInfoFromMySQL.getInfo('user_info', 'user_name', user_name, 0, 'show')
        _type = type(seat)
        print("type(seat)",_type)

        if(seat==''):#??
            judge=0


        # 航班信息展示,输入航班信息就能确定位置
        print("input flight_ID ")
        # flight_ID = input()
        flight_ID = 'A1'
        sql_select_flight = "select * from airplane where flight_ID='%s'" % flight_ID
        cursor1.execute(sql_select_flight)
        rs = cursor1.fetchall()
        for row in rs:
            leftover = row[1]
        if(leftover<150 and judge==1):
            # 修改表1主航班的flight_ID修改，提交保存leftover+1的表
            if (cancel_ticket == 1):
                leftover += 1
                sql_cancel_ticket = "update airplane set leftover=%d where flight_ID='%s' " % (leftover, flight_ID)
                cursor1.execute(sql_cancel_ticket)
                print("cancel success")
            if (cancel_ticket == 0):
                print("cancel exit sucess")

            seat=getInfoFromMySQL.getInfo('user_info', 'user_name', user_name, 0, 'NULL')
            # 修改表2空座位信息，详细表座位信息修改,
            sql_update = "update %s set empty=1 where seat='%s'" % (flight_ID, seat)
            cursor1.execute(sql_update)  # print(sql_update)
            db.commit()

            sql_update = "update user_info set seat='',flight_ID='' where user_name='%s'" % user_name
            cursor1.execute(sql_update)
            db.commit()
            print("客户信息")
            print("ID||user_name||user_password||seat||flight_ID")
            getInfoFromMySQL.getInfo('user_info', 'user_name', user_name, 0, 'show')
        else:
            print("已经cancel,不能重复")

    except Exception as e:
        print(e)
        db.rollback()
    cursor1.close()
    db.commit()
    db.close()

# cancel_ticket(user_name='Zheng')



