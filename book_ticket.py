import pymysql
import getInfoFromMySQL
def book_ticket(user_name='Zheng'):  # 订阅特定航班，先展示特定航班座位空的信息
    db = pymysql.connect("localhost", "root", "", "new_schema")
    cursor = db.cursor()
    judge=1
    try:
        # 航班信息展示
        # print("book ticket?please input flight_ID ")
        # flight_ID=input()
        flight_ID='A1'
        print("具体某一航班信息展示，此为%s"%flight_ID)
        # flight_ID.lower()
        try:
            sql_select_flight="select * from %s where empty=1"%flight_ID
            cursor.execute(sql_select_flight)
            rs=cursor.fetchall()
            print("flight_ID|| seat ")
            for row in rs:
                print(row[0:2])

        except Exception as e:
            print(e)
            db.rollback()

        cursor.close()#另起一个游标先



        cursor1=db.cursor()
         #1、订票,牵涉3张 表：1)主表airplane座位剩余leftover 2){航班具体座位信息 flight_A1 :)1)seat  ))2.empty  }
         #                     3){客户user_info表 :))1.航班 flight_ID ))2.座位 seat}

        print("想要什么座位")
        # book_=input()
        book_=1
        book_=int(book_)
        if(book_==1):
            # book_=input()

            seat = getInfoFromMySQL.getInfo('user_info', 'user_name', user_name, 0, 'show')

            if(seat!=''):
                judge=0




            if(judge==1):
                seat = 'a1'
                print("座位", seat)

            # print("input the seat wanted %s"%seat)
            #修改座位
            # 1、订票,牵涉3张 表：1)主表airplane座位剩余leftover 2){航班具体座位信息 flight_A1 :)1)seat  ))2.empty  }
            #                     3){客户user_info表 :))1.航班 flight_ID ))2.座位 seat}
            #1、1)主表airplane座位剩余leftover
            # print("订座成功，您的航班信息")

            #修改三张表,有
                choice='alter --'
                #修改1表主航班,leftover
                sql_select_flight = "select * from  airplane where flight_ID='%s'" %seat

                cursor1.execute(sql_select_flight)
                rs=cursor1.fetchall()
                try:
                    for row in rs:
                        leftover = row[1]

                    # 更新后数据
                    leftover = int(leftover)
                    leftover -= 1
                    sql_update = "update airplane set leftover=%d where flight_ID='%s' " % (leftover, flight_ID)
                    cursor1.execute(sql_update)
                    db.commit()
                    #更新后数据展示
                except Exception as e:
                    print(e)
                    db.rollback()


                #修改表2空座位信息，详细表座位信息修改,

                sql_update = "update %s set empty=0 where seat='%s'" % (flight_ID, seat)
                cursor1.execute(sql_update)

                # 修改表3){客户user_info表 :))1.航班 flight_ID ))2.座位 seat}
                sql_update = "update user_info set seat='%s',flight_ID='%s' where user_name='%s'" % (seat, flight_ID, user_name)
                cursor1.execute(sql_update)
                db.commit()
                print("客户信息")
                print("ID||user_name||user_password||seat||flight_ID")
                getInfoFromMySQL.getInfo('user_info', 'user_name', user_name, 0, 'show')
            else:
                print("您已经已经订过此票了")

    except Exception as e:
        print(e)
        db.rollback()
    #??老是报cursor closed
    cursor1.close()
    db.commit()
    db.close()

# book_ticket(user_name='Zheng')