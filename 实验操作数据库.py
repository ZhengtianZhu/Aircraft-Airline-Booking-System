import pymysql
db=pymysql.connect("localhost","root","","new_schema")
cursor1=db.cursor()



seat='a1'
flight_ID='a1'

import getInfoFromMySQL
user_name='Zheng'

# sql_update = "update user_info set seat='a1',flight_ID='a1' where user_name='%s'"%user_name
# cursor1.execute(sql_update)
# print("客户信息")
# print("ID||user_name||user_password||seat||flight_ID")
# getInfoFromMySQL.getInfo('user_info', 'user_name', user_name, 0, 'show')


cursor1.close()
db.commit()
db.close()