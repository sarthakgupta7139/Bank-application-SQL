import mysql.connector
import sys

def searchAccount(acno):
    con = giveConnection()
    cursor=con.cursor()
    qry="select * from customer where acno={}".format(acno)
    cursor.execute(qry)
    row=cursor.fetchone()
    n=cursor.rowcount
    if n>0:
        return True
    else:
        return False


def addAC():
    con=giveConnection()
    acno=int(input('Enter A/C no:'))
    cname=input('Enter name:')
    actype=input('Enter A/c type (saving/current):')
    bal=int(input('Enter opening balance:'))
    cursor = con.cursor()

    qry = "insert into customer values({},'{}','{}',{})".format(acno, cname, actype, bal)
    cursor.execute(qry)
    con.commit()
    con.close()

def deposit():
    con=giveConnection()
    acc=int(input('Enter A/c no.:'))
    cursor=con.cursor()
    if searchAccount(acc)==True:
        money = int(input('Enter money to deposit:'))
        qry="update customer set bal=bal+{} where acno={}".format(money,acc)
        cursor.execute(qry)
        print('Money is deposited.')
        con.commit()
        con.close()
    else:
        print('A/c not found.')

def withdraw():
    con=giveConnection()
    acc=int(input('Enter A/c no.:'))
    if searchAccount(acc)==True:
        money=int(input('Enter money to withdraw:'))
        cursor=con.cursor()
        qry="update customer set bal=bal-{} where acno={}".format(money,acc)
        print('Money is withdrawn.')
        cursor.execute(qry)
        con.commit()
        con.close()
    else:
        print('A/c not found.')

def enquiryAC():
    con=giveConnection()
    acc=int(input('Enter A/c no:'))
    if searchAccount(acc)==True:
        cursor=con.cursor()
        qry="select * from customer where acno ={}".format(acc)
        cursor.execute(qry)
        x=cursor.fetchall()
        print('=' * 50)
        print('A/c no. no is {}'.format(x[0][0]))
        print('Customer name is {}'.format(x[0][1]))
        print('A/c is {} type'.format(x[0][2]))
        print('A/c balance is {}'.format(x[0][3]))
    else:
        print('A/c not found.')

def displayAll():
    con = giveConnection()
    cursor=con.cursor()
    qry="select * from customer"
    cursor.execute(qry)
    rec=cursor.fetchall()
    print('=' * 50)

    for x in rec:
        print('A/c no. no is {}.'.format(x[0]))
        print('Customer name is {}.'.format(x[1]))
        print('A/c is {} type.'.format(x[2]))
        print('A/c balance is {}'.format(x[3]))
        print('='*50)

    con.close()

def closeAC():
    con=giveConnection()
    acc = int(input('Enter A/c no. to delete:'))
    if searchAccount(acc)==True:
        cursor = con.cursor()
        qry = "delete from customer where acno={}".format(acc)
        print('A/c closed successfully.')
        cursor.execute(qry)
        con.commit()
        con.close()
    else:
        print('A/c not found.')

def closeAll():
    con=giveConnection()
    cursor = con.cursor()
    qry = "delete from customer"
    print('All A/c are deleted.')
    cursor.execute(qry)
    con.commit()
    con.close()

def giveConnection():
    con = mysql.connector.connect(host='localhost', database='bank', user='root', password='')
    return con

while True:
    print('=' * 50)
    print('Main Menu:')
    print('1. Add A/c')
    print('2. Deposit Money')
    print('3. Withdraw Money')
    print('4. Enquiry A/c')
    print('5. Display All')
    print('6. Close A/c')
    print('7. Close All A/c')
    print('8. Exit')
    choice=int(input('Enter your choice:'))
    if choice==1:
        addAC()

    elif choice==2:
        deposit()

    elif choice==3:
        withdraw()

    elif choice==4:
        enquiryAC()

    elif choice==5:
        displayAll()

    elif choice==6:
        closeAC()

    elif choice==7:
        closeAll()

    elif choice==8:
        sys.exit(0)

    else:
        print('Invalid choice')