#!!特地在这里git
import pymysql
import fileinput
import cancel_ticket
import log_in
import book_ticket
import getInfoFromMySQL

#输入
def main():


    print("please log_in")
    user_name=log_in.log_in()
    #??pydev debugger: process 8328 is connecting

    #选择界面循环
    choice=1
    while choice!=0:
        print("function:3.view table airplane 4.order  6.book_ticket 7.cancel_ticket")
        # _input=input()
        _input=4
        if(_input==3):
            getInfoFromMySQL.getInfo('airplane','flight_ID','NULL',0,'all airplane')
        if(_input==4):
            getInfoFromMySQL.getInfo('airplane','flight_ID','NULL',0,'order des airplane')
        if(_input==5):
            break # find()
        if(_input==6):
            book_ticket.book_ticket(user_name)
        if(_input==7):
            cancel_ticket.cancel_ticket(user_name)
        #提示是否跳出选择界面循环
        print("want to exit,enter make choice ==0 else enter 1 to continue")
        choice = input()
        choice=int(choice)
        if(choice==1):
            continue
        else:
            break




    
main()

