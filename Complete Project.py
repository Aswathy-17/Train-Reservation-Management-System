import mysql.connector as mycn
mydb = mycn.connect(host='localhost', user='root', password='shnroot')
mycursor = mydb.cursor()
sql0='create database if not exists project;'
mycursor.execute(sql0)
sql01='use project;'
mycursor.execute(sql01)
s='drop table reservation1'     #When running Code for the first time delete 
s1='drop table train'           #
mycursor.execute(s)             #
mycursor.execute(s1)            #till here and then copy it back
sql28 = 'create table if not exists user(user_id varchar(10),password varchar(15),Name varchar(30));'
mycursor.execute(sql28)
sql29 = 'insert into user values ("User1","us123","Brian");'
mycursor.execute(sql29)

def mod():
    print("_____________________________")
    print("\t \t MENU \n")
    print("_____________________________")
    print("1. Modify Destination \n")
    print("2. Modify Start Point \n")
    print("3. Modify Date \n")
    print("4. Back \n")
    print("5. Exit \n")
    op3=input("Enter Your Option: ")
    if op3=='5':
        exit()
    if op3=='4':
        main()
    if op3=='1':
        print("Modify Destination Selected")
        print("___________________________________________________________________")
        print("Ticket Details")
        mycursor.execute(f"SELECT * FROM reservation1 Where PNR='{n}'")
        myresult=mycursor.fetchall()
        print(myresult)
        des=input("Enter New Destination: ")
        yn=input("Do You Confirm(Yes/No): ")
        if yn=="Yes" or yn=="YES" or yn=="yes":
            sql50="update reservation1 set Destination=%s where PNR=%s;"
            valu = (des,n)
            mycursor.execute(sql50,valu)
            mydb.commit()
            print("Reservation Updated")
            main()
    if op3=='2':
        print("Modify Start Point Selected")
        print("__________________________________")
        mycursor.execute("select * from reservation1 where PNR='%s'"%n)
        myresult=mycursor.fetchone()
        print(myresult)
        st=input("Enter New Start Point: ")
        yn=input("Do You Confirm(Yes/No): ")
        if yn=="Yes" or yn=="YES" or yn=="yes":
            sql51="update reservation1 set Start_Point=%s where PNR=%s;"
            valu=(st,n)
            mycursor.execute(sql51,valu)
            mydb.commit()
            print("Reservation Updated")
            main()
    if op3=='3':
        print("Modify Date Selected")
        print("__________________________________")
        mycursor.execute("select * from reservation1 where PNR='%s'"%n)
        myresult=mycursor.fetchone()
        print(myresult)
        dt=input("Enter New Date:yyyy-mm-dd: ")
        yn=input("Do You Confirm(Yes/No): ")
        if yn=="Yes" or yn=="YES" or yn=="yes":
            sql52="update reservation1 set Date_of_journeyt=%s WHERE PNR=%s;"
            valu=(dt,n)
            mycursor.execute(sql52,valu)
            mydb.commit()
            print("Reservation Updated")   # modify
            main()
    else:
        print("Invalid Input")
        print("Please Try Again")

def delt():
    yn=input("Do You Want To Confirm?(Yes,No): ")
    if yn=='YES' or yn=='yes' or yn=='Yes':
        mycursor.execute("delete from reservation1 where PNR='%s'" %d)
        print("Reservation Cancelled")
        if 1610850011 < d < 1610850031 :
            reserve_first.pop()
            conpnr.remove(d)
            main()
        elif 1610850031 < d < 1610850051 :
            reserve_second.pop()
            conpnr.remove(d)
            main()
        elif 1610850051 < d < 1610850071 :
            reserve_third.pop()
            conpnr.remove(d)
            main()
        elif 1610850071 < d < 1610850091 :
            reserve_firstac.pop()
            conpnr.remove(d)
            main()
        elif 1610850091 < d < 1610850111 :
            reserve_secondac.pop()
            conpnr.remove(d)
            main()
        elif 1610850111 < d < 1610850131 :
            reserve_thirdac.pop()
            conpnr.remove(d)
            main()
        elif 1610850131 < d < 1610850151 :
            reserve_sleeper.pop()
            conpnr.remove(d)
            main()
    elif yn=='No' or yn=='no' or yn=='NO':
        print("Terminated Succesfully")             # delete
        main()
    else:
        print("Invalid Input")
        print("Try Again")
        delt()

def tablecr():
    sql = 'create table if not exists train(Train_Name varchar(50), Train_No integer PRIMARY KEY, Date_of_Journey date, Start_Point varchar(50), Destination varchar(50));'
    mycursor.execute(sql)
    sql1 = 'insert into train values ("Telangana Ap Express", 12724, "2020-10-15", "Hyderabad", "New Delhi");'
    mycursor.execute(sql1)
    sql2 = 'insert into train values ("Tamil Nadu Express", 12621, "2020-10-15", "Chennai", "New Delhi");'
    mycursor.execute(sql2)
    sql3= 'insert into train values ("Rajdhani Express", 22691, "2020-10-15", "Bangalore", "New Delhi");'
    mycursor.execute(sql3)
    sql4= 'insert into train values ("Mangladweep Express", 22617, "2020-10-16", "Ernakulam", "Nizamuddin");'
    mycursor.execute(sql4)
    sql5= 'insert into train values ("Netravathi Express", 26346, "2020-10-16", "Ernakulam", "Madgaon");'
    mycursor.execute(sql5)
def recr():
    sql27 ='Create table if not exists reservation1(PNR integer PRIMARY KEY,Passenger_Name varchar(30), Start_point varchar(20), Destination varchar(20), Date_of_journey date,Class varchar(20));'
    mycursor.execute(sql27)
recr()                      #table creation
tablecr()
def login():
    print("_____________________________________________________________________________")
    print("\t\t LOGIN as: \n")
    print("1. ADMIN \n")
    print("2. USER \n")
    op =input("Enter Option: ")
    if op == '1':
        loginadm()
    if op == '2':
        loginuser()
    else:
        print("Invalid Input")
        print("Please Try Again")
        login()

def main():                          
    while True:
        print("___________________________________")
        print("\t \t MENU \n")
        print("1. Book Train Tickets \n")
        print("2. Check PNR Status \n")
        print("3. Change booking details \n")
        print("4. Cancel Booking \n")
        print("5. Back \n")
        print("6. Exit \n")
        op = input("Enter your option: ")

        if op == '6':
            exit()  

        elif op == '1':
            p = input("Passenger's Name: ")
            dt = input("Date of journey: yyyy-mm-dd : ")
            while len(dt)!=10:
                    print("Invalid Input")
                    print("Plese Enter Again")
                    dt=input("Date of journey: yyyy-mm-dd :")
            mycursor.execute("select distinct(Train_Name) , Train_No , Start_Point , Destination from train where Date_of_journey='%s'" % dt)
            myresult = mycursor.fetchall()
            print("_______________________________________________________________________________________________________")
            print("%15s" %"Train Name            ","%15s" %"Train Number  ","%15s"% "Start Point  ","%15s" %"Destination")
            print("_______________________________________________________________________________________________________")
            for x in myresult:
                print("%15s" %x[0],"%15s" %x[1],"%15s" %x[2],"%15s" %x[3])
            print("_______________________________________________________________________________________________________")
            sp = input("Select Start Point: ")
            mycursor.execute(f"SELECT * FROM train Where Start_Point='{sp}'")
            result1 = mycursor.fetchall()
            if result1: 
                d = input("Select Destination: ")
                mycursor.execute(f"SELECT * FROM train Where Destination='{d}'")
                result2 = mycursor.fetchall()
                if result2:
                    print("\n Available Classes")
                else:
                    print("Sorry. . .")
                    print("No Such Destination")
                    print("Try Again")
                    main()
            else:
                print("Sorry. . .")
                print("No Such Start Point")
                print("Try Again")
                main()
            print("\n")
            print("__________________________________")
            print(" CLASS            BASE PRICE \n")
            print("__________________________________")
            print("First              100rs \n")
            print("Second             80 rs \n")
            print("Third              60 rs \n")
            print("First AC           130rs \n")
            print("Second AC          110rs \n")
            print("Third AC           90 rs \n")
            print("Sleeper AC         150rs \n")
            print("__________________________________")
            c = input("Select Class: ")
            confirm= input("Do you want to confirm ? (Yes/No): ")
            if confirm== 'Yes' or 'yes':
                if c == 'First' or c == 'first':
                    for i in range(1, 22):  # range(1 to 21)
                        if i == 21:
                            print("No available seats")
                            exit()
                        if i in reserve_first:
                            continue
                        elif i != 21:
                            reserve_first.append(i)
                            seat = i
                            coach = 1
                            pnr = 1610850010 + coach + i  # PNR values from 1610850012-1610850031
                            break
                if c == 'Second' or c == 'second':
                    for i in range(1, 21 + 1):
                        if i == 21:
                            print("No available seats")
                            exit()
                        if i in reserve_second:
                            continue
                        elif i != 21:
                            reserve_second.append(i)
                            seat = i
                            coach = 2
                            pnr = 1610850029 + coach + i  # PNR values from 1610850032-1610850051
                            break
                if c == 'Third' or c == 'third':
                    for i in range(1, 21 + 1):
                        if i == 21:
                            print("No available seats")
                            exit()
                        if i in reserve_third:
                            continue
                        elif i != 21:
                            reserve_third.append(i)
                            seat = i
                            coach = 3
                            pnr = 1610850048 + coach + i  # PNR values from 1610850052-1610850071
                            break
                if c == 'First AC' or c == 'first ac':
                    for i in range(1, 21 + 1):
                        if i == 21:
                            print("No available seats")
                            exit()
                        if i in reserve_firstac:
                            continue
                        elif i != 21:
                            reserve_firstac.append(i)
                            seat = i
                            coach = 4
                            pnr = 1610850067 + coach + i  # PNR values from 1610850053-1610850091
                            break
                if c == 'Second AC' or c == 'second ac':
                    for i in range(1, 21 + 1):
                        if i == 21:
                            print("No available seats")
                            exit()
                        if i in reserve_secondac:
                            continue
                        elif i != 21:
                            reserve_secondac.append(i)
                            seat = i
                            coach = 5
                            pnr = 1610850086 + coach + i  # PNR values from 1610850092-1610850111
                            break
                if c == 'Third AC' or c == 'third ac':
                    for i in range(1, 21 + 1):
                        if i == 21:
                            print("No available seats")
                            exit()
                        if i in reserve_thirdac:
                            continue
                        elif i != 21:
                            reserve_thirdac.append(i)
                            seat = i
                            coach = 6
                            pnr = 1610850105 + coach + i  # PNR values from 1610850112-1610850131
                            break
                if c == 'Sleeper' or c == 'sleeper':
                    for i in range(1, 21 + 1):
                        if i == 21:
                            print("No available seats")
                            exit()
                        if i in reserve_sleeper:
                            continue
                        elif i != 21:
                            reserve_sleeper.append(i)
                            seat = i
                            coach = 7
                            pnr = 1610850124 + coach + i  # PNR values from 1610850132-1610850151
                            break
            else:
                print("Terminated")
                main()
            sql30 = "insert into reservation1 (PNR,Passenger_Name,Start_point,Destination,Date_of_journey,Class) values (%s,%s,%s,%s,%s,%s);"
            val = (pnr,p, sp, d, dt, c)
            mycursor.execute(sql30, val)  # inserts row into reservation table
            mydb.commit()  # makes changes permanent on confirmation
            def pay():
                po = input("Proceed to pay (Yes/No) : ")
                if po == 'Yes' or po == 'yes' or po=='YES':
                    print("_____________________________")
                    print("Pay with \n")
                    print("1. Credit card \n")
                    print("2. Debit card \n")
                    print("3. Bank transfer \n")
                    print("_____________________________")
                    op1 = int(input("Payment option: "))
                    if op1 == 1 or op1 == 2 or op1 == 3:
                        print("Payment Successful")
                        print("Train Tickets Successfully Booked !")
                        print("Passenger's Name: ", p)
                        print("Seat No :", seat)
                        print("Coach No :", coach)
                        print("PNR No :", pnr)
                        conpnr.append(pnr)
                elif po=='No' or po=='NO' or po=='no':
                    print("Payment Declined")
                else:
                    print("Invalid Input")
                    print("Please Try Again")
                    pay()
            pay()
        elif op == '2':
            def pnr():
                pn =int(input("Enter 10 digit PNR: "))
                s=str(pn)
                l=len(s)
                if l==10:  
                    if pn in conpnr:
                        print("Seat Confirmed")
                        mycursor.execute("select * from reservation1 where PNR='%s'"%pn)
                        myresult=mycursor.fetchone()
                        print(myresult)
                        print('\n')
                    else:
                        print("Seat Not Confirmed")
                else:
                    print("PNR Error")
                    print("Check PNR and Try")
                    pnr()
            pnr()
        elif op == '3':
            def mo():
                global n
                n=int(input("Enter PNR: "))
                l=len(str(n))
                if l!=10:
                    print("INCORRECT PNR")                                      #DELETION
                    print("PLEASE TRY AGIAN !!")
                else:
                    mycursor.execute("select PNR from reservation1")
                    rslt=mycursor.fetchall()
                    for i in rslt:
                        for w in i:
                            if w==n:
                                mod()
                    else:
                        print("INCORRECT PNR")
                        print("PLEASE TRY AGIAN !!")
                        mo()
            mo()
               
        elif op == '4':
            def pnrtst():
                print("_____________________________")
                print("DELETION WITH PNR")
                print("_____________________________")
                global d
                d=int(input("Enter PNR: "))
                l=len(str(d))
                if l!=10:
                    print("INCORRECT PNR")                                      #DELETION
                    print("PLEASE TRY AGIAN !!")
                else:
                    mycursor.execute("select PNR from reservation1")
                    rslt=mycursor.fetchall()
                    for i in rslt:
                        for w in i:
                            if w==d:
                                delt()
                    else:
                        print("INCORRECT PNR")
                        print("PLEASE TRY AGIAN !!")
                        pnrtst()            
            pnrtst()
        elif op == '5':
            login()
                                                                                           #main user part ending
        else:
            print("Invalid Input")
            print("Please Try Again!")
            main()
           
def upd():
        print("_____________________________________________________________________________")
        print('\t\t MODIFY USING: \n')
        print("1. Train Name \n")
        print("2. Train Number \n")
        print("3. Back \n")
        op=input("Enter Option: ")
        if op=='3':
            main2()
        if op=='1':
            print("_____________________________________________________________________________")
            print("\t Update\n")
            print("1. Train Number \n")
            print("2. Date Of Journey \n")
            print("3. Start Point \n")
            print("4. Destination \n")
            print("5. Back \n")
            op1=input("Enter Option To Modify: ")
            if op1=='5':
                main2()
            if op1=='1':
                def utrno():
                    train_name=input("Enter Train Name: ")
                    mycursor.execute(f"SELECT * FROM train Where Train_Name='{train_name}'")
                    result = mycursor.fetchone()
                    print(result)
                    if result:
                        train_no=int(input("Enter New Train Number: "))
                        val1=(train_no,train_name)
                        sql1="update train set train_no=%s where train_name=%s;"
                        mycursor.execute(sql1,val1)
                        mydb.commit()
                        print("DETAILS MODIFIED !")
                        main2()
                    else:
                        print("No Such Train exists")
                        print("Try Again")
                        utrno()
                utrno()
            if op1=='2':
                def utrd():
                    train_name=input("Enter Train Name: ")
                    mycursor.execute(f"SELECT * FROM train Where Train_Name='{train_name}'")
                    result = mycursor.fetchone()
                    print(result)
                    if result:
                        date=input("Enter New Date Of Journey: ")
                        while len(date)!=10:
                            print("Invalid Input")
                            print("Plese Enter Again")
                            date=input("Enter New Date Of Journey: ")
                        val2=(date,train_name)
                        sql2="update train set date_of_journey=%s where train_name=%s;"
                        mycursor.execute(sql2,val2)
                        mydb.commit()
                        print("DETAILS MODIFIED !")
                        main2()
                    else:
                        print("No Such Train Exists")
                        print("Try Again")
                        utrd()
                utrd()
            if op1=='3':
                def usp():
                    train_name=input("Enter Train Name: ")
                    mycursor.execute(f"SELECT * FROM train Where Train_Name='{train_name}'")
                    result = mycursor.fetchone()
                    print(result)
                    if result:                    
                        start_point=input("Enter New starting point: ")
                        val3=(start_point,train_name)
                        sql3="update train set start_point=%s where train_name=%s;"
                        mycursor.execute(sql3,val3)
                        mydb.commit()
                        print("DETAILS MODIFIED !")
                        main2()
                    else:
                        print("No Such Train Exists")
                        print("Try Again")
                        usp()
                usp()
            if op1=='4':
                def ud():
                    train_name=input("Enter Train Name: ")
                    mycursor.execute(f"SELECT * FROM train Where Train_Name='{train_name}'")
                    result = mycursor.fetchone()
                    print(result)
                    if result:
                        destination=input("Enter New Destination: ")
                        val4=(destination,train_name)
                        sql4="update train set destination=%s where train_name=%s;"
                        mycursor.execute(sql4,val4)
                        mydb.commit()
                        print("DETAILS MODIFIED !")
                        main2()
                    else:
                        print("No Such Train Exists")
                        print("Try Again")                        
                        ud()
                ud()
        if op=='2':
            print("_____________________________________________________________________________")
            print("\t Update \n")
            print("1. Train Name \n")
            print("2. Date Of Journey \n")
            print("3. Start Point \n")
            print("4. Destination \n")
            print("5. Back \n")
            op2=input("Enter Option To Modify: ")
            if op2=='5':
                main2()
            if op2=='1':
                def ut1():
                    train_no=int(input("Enter Train Number: "))
                    mycursor.execute(f"SELECT * FROM train Where Train_No='{train_no}'")
                    result = mycursor.fetchone()
                    print(result)
                    if result:                    
                        train_name=input("Enter New Train Name: ")
                        val5=(train_name,train_no)
                        sql5="update train set train_name=%s where train_no=%s;"
                        mycursor.execute(sql5,val5)
                        mydb.commit()
                        print("DETAILS MODIFIED !")
                        main2()
                    else:
                        print("No Such Train Number Exists")
                        print("Try Again")
                        ut1()
                ut1()
            if op2=='2':
                def ut2():
                    Train_no=int(input("Enter Train Number: "))
                    mycursor.execute(f"SELECT * FROM train Where Train_No='{train_no}'")
                    result = mycursor.fetchone()
                    print(result)
                    if result:                                        
                        date=input("Enter New Date Of Journey: ")
                        while len(date)!=10:
                            print("Invalid Input")
                            print("Plese Enter Again")
                            date=input("Enter New Date Of Journey: ")
                        val6=(date,train_no)
                        sql6="update train set date_of_journey=%s where train_no=%s;"
                        mycursor.execute(sql6,val6)
                        mydb.commit()
                        print("DETAILS MODIFIED !")
                        main2()
                    else:
                        print("No Such Train Number Exists")
                        print("Try Again")
                        ut2()
                ut2()
            if op2=='3':
                def ut3():
                    Train_no=int(input("Enter Train Number: "))
                    mycursor.execute(f"SELECT * FROM train Where Train_No='{train_no}'")
                    result = mycursor.fetchone()
                    print(result)
                    if result:                                        
                        start_point=input("Enter  New Starting Point: ")
                        val7=(start_point,train_no)
                        sql7="update train set start_point=%s where train_no=%s;"
                        mycursor.execute(sql7,val7)
                        mydb.commit()
                        print("DETAILS MODIFIED !")
                        main2()
                    else:
                        print("No Such Train Number Exists")
                        print("Try Again")
                        ut3()
                ut3()
            if op2=='4':
                def ut4():
                    Train_no=int(input("Enter Train Number: "))
                    mycursor.execute(f"SELECT * FROM train Where Train_No='{train_no}'")
                    result = mycursor.fetchone()
                    print(result)
                    if result:                                        
                        destination=input("Enter New Destination: ")
                        val8=(destination,train_no)
                        sql8="update train set destination=%s where train_no=%s;"
                        mycursor.execute(sql8,val8)
                        mydb.commit()
                        print("DETAILS MODIFIED !")
                        main2()
                    else:
                        print("No Such Train Number Exists")
                        print("Try Again")
                        ut4()
                ut4()
def loginadm():
        while True:
            us=input("Enter Username: ")
            if us=='adm':
                while True:
                    pwd=input("Enter Password: ")
                    if pwd=='123adm':
                        print("LOGGED IN !")
                        main2()
                    else:
                        print("Incorrect Password !")
                        print("Retry !")
                        print("\n")
                        continue
                break
            else:
                print("Incorrect Username !")
                print("Retry !")
                print("\n")
                continue
def insrt():
    print("_____________________________________________________________________________")
    print("\t INSERTION: \n")
    def tno1():
        to=int(input("Enter Train No: "))
        mycursor.execute(f"SELECT * FROM train Where Train_No='{to}'")
        result = mycursor.fetchone()
        print(result)
        if result:
            print("This Train Number Already Exists")
            print("Try Again")
            tno1()
        else:
            def tname1():
                tn=input("Enter Train Name: ")
                mycursor.execute(f"SELECT * FROM train Where Train_Name='{tn}'")
                result1 = mycursor.fetchone()
                print(result1)
                if result1:
                    print("This Train Already Exists")
                    print("Try Again")
                    tname1()
                else:
                    dj=input("Enter Date Of Journey (yyyy-mm-dd): ")
                    sp=input("Enter Start Point: ")
                    de=input("Enter Destination: ")
                    sql36="insert into train values(%s,%s,%s,%s,%s);"
                    val5=(tn,to,dj,sp,de)
                    mycursor.execute(sql36,val5)
                    print("SUCCESSFULLY INSERTED !")
                    q2=input("Insert More (Yes/No): ")                 # INSERTION
                    if q2=='yes' or q2=='Yes':
                        insrt()
                    elif q2=='No' or q2=='no':
                        main2()
            tname1()
    tno1()                    
def loginuser():
    print("_____________________________________________________________________________")
    print("\t LOG-IN: \n")
    print("1. Create An Account \n")
    print("2. Sign-In \n")
    print("3. Back \n")
    op5=input("Enter Option: ")
    if op5=='3':
        login()
    if op5=='1':
        def crte():
            print("_____________________________________________________________________________")
            print("\t CREATE ACCOUNT: \n")
            u=input("Enter Username: ")
            n=input("Enter Name: ")
            p=input("Enter Password: ")
            val6=(u,p,n)
            sql37=('insert into user values (%s,%s,%s);')
            q3=input("Confirm Account Creation (Yes/No): ")                             # CREATING ACCOUNT
            if q3=='Yes' or q3=='yes':
                mycursor.execute(sql37,val6)
                print("Account Created ! \n")
                print("***** HELLO ",n ,'***** \n')
                main()
            elif q3=='No' or q3=='no':
                print("Create Account Again To Continue !")
                crte()
        crte()
    if op5=='2':
        while True:
            user_name = input("Enter User Name: ")
            user_pass = input("Enter Password: ")
            sql30 = 'select user_id from user;'
            mycursor.execute(sql30)
            myresult01 = mycursor.fetchall()
            if (user_name, ) in myresult01:
                mycursor.execute("select Name from user where user_id='%s'" % user_name)
                myresult02 = mycursor.fetchall()
                for k in myresult02:
                    NAME=k[0]
                mycursor.execute("select password from user where user_id='%s'" % user_name)
                myresult03 = mycursor.fetchall()
                pwd = myresult03
                if (user_pass, ) in pwd:
                    print("Login Confirmed")
                    print("HELLO ", NAME, "!")
                    main()
                else:
                    print("Invalid User Name or Password")
                    print("Please Try Again")
            else:
                print("Invalid User Name or Password")
                print("Please Try Again")
    else:
        print("Invalid Input")
        print("PLEASE TRY AGIAN")
        loginuser()
def delete():
            print("_____________________________________________________________________________")
            print("\t DELETE USING: \n")
            print("1. Train Name \n")
            print("2. Train No \n")
            print("3. Date Of Journey \n")
            print("4. Start Point \n")
            print("5. Destination \n")
            print("6. Back \n")
            op4=int(input("Enter Option To Delete: "))
            if op4==6:
                main2()
            if op4==1:
                def a1():
                    train_name=input("Enter Train Name: ")
                    mycursor.execute(f"SELECT * FROM train Where Train_Name='{train_name}'")
                    result1 = mycursor.fetchone()
                    print(result1)
                    if result1:   
                        mycursor.execute("delete from train where train_name='%s';"%train_name)
                        mydb.commit()
                        print("SUCCESSFULLY DELETED !")
                        main2()
                    else:
                        print("No Such Train Exists")
                        print("Try Again")
                        a1()
                a1()
            if op4==2:
                def a2():
                    train_no=int(input("Enter Train No: "))
                    mycursor.execute(f"SELECT * FROM train Where Train_No='{train_no}'")
                    result1 = mycursor.fetchone()
                    print(result1)
                    if result1:                    
                        mycursor.execute("delete from train where train_no='%s';"%train_no)
                        mydb.commit()
                        print("SUCCESSFULLY DELETED !")
                        main2()
                    else:
                        print("No Such Train Number")
                        print("Try Again")
                        a2()
                a2()
            if op4==3:                                                          # DELETION
                def a3():
                    date=input("Enter Date Of Journey: ")
                    mycursor.execute(f"SELECT * FROM train Where Date_of_Journey='{date}'")
                    result1 = mycursor.fetchone()
                    print(result1)
                    if result1:                    
                        mycursor.execute("delete from train where date_of_journey='%s';"%date)
                        mydb.commit()
                        print("SUCCESSFULLY DELETED !")
                        main2()
                    else:
                        print("No Such Date Exists Here")
                        print("Try Again")
                        a3()
                a3()
            if op4==4:
                def a4():
                    start_point=input("Enter Starting Point: ")
                    mycursor.execute(f"SELECT * FROM train Where Start_Point='{start_point}'")
                    result1 = mycursor.fetchone()
                    print(result1)
                    if result1:                    
                        mycursor.execute("delete from train where start_point='%s';"%start_point)
                        mydb.commit()
                        print("SUCCESSFULLY DELETED !")
                        main2()
                    else:
                        print("No Such Starting Point")
                        print("Try Again")
                        a4()
                a4()
            if op4==5:
                def a5():
                    Destination=input("Enter Destination: ")
                    mycursor.execute(f"SELECT * FROM train Where Train_No='{train_no}'")
                    result1 = mycursor.fetchone()
                    print(result1)
                    if result1:                    
                        mycursor.execute("delete from train where destination='%s';"%destination)
                        mydb.commit()
                        print("SUCCESSFULLY DELETED !")
                        main2()
                    else:
                        print("No Such Destination")
                        print("Try Again")
                        a5()
                a5()
            else:
                print("Invalid Input")
                print("PLEASE TRY AGIAN")
                delete()
def shtable():
    mycursor.execute("select * from train;")
    myresult = mycursor.fetchall()
    print("_______________________________________________________________________________________________________")
    print("%15s" %"Train Name","%20s" %"Train Number","%15s" %"Date","%15s"% "Start Point","%15s" %"Destination")
    print("_______________________________________________________________________________________________________")
    for i in myresult:
        print("%15s" %i[0],"%15s" %i[1],"%15s" %i[2],"%15s" %i[3],"%15s" %i[4])
    print("_______________________________________________________________________________________________________")
    main2()
def main2():
    print("_____________________________________________________________________________")
    print("\t CHOOSE: \n")
    print("1. Update Stats \n")
    print("2. Delete Stats \n")
    print("3. Insert New Stats \n")
    print("4. Show Table Stats \n")
    print("5. Back \n")
    print("6. Exit \n")
    op1=input("Enter Option: ")
    if op1=='1': #modify
        upd()
    if op1=='2': #delete
        delete()
    if op1=='3': #insert
        insrt()
    if op1=='4':
        shtable()
    if op1=='5':
        login()
    if op1=='6':
        exit()
    else:
        print("Invalid Input")
        print("PLEASE TRY AGAIN")
        main2()

        # THE CODE STARTS HERE!
conpnr = []
reserve_first = []
reserve_second = []
reserve_third = []
reserve_firstac = []
reserve_secondac = []
reserve_thirdac = []
reserve_sleeper = []
login()
