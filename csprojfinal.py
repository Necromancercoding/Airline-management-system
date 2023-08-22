import pymysql
import time
import random
db=pymysql.connect(host='localhost',user='root',password='root@1234')
cur=db.cursor()
cur.execute('use trial')

BLS=["1A","1B","1C","1D","2A","2B","2C","2D","3A","3B","3C","3D","4A","4B","4C","4D","5A","5B","5C","5D","6A","6B","6C","6D","6E","7A","7B","7C","7D","7E","8A","8B","8C","8D","8E","9A","9B","9C","9D","9E","10A","10B","10C","10D","10E"]#seat layout for business
BINLISTK=['CN1', 'CN2', 'CN3', 'CN4', 'CN5', 'CN6', 'CN7', 'CN8', 'CN9', 'CN10', 'CN11', 'CN12', 'CN13', 'CN14', 'CN15', 'CN16', 'CN17', 'CN18', 'CN19', 'CN20', 'CN21', 'CN22', 'CN23', 'CN24', 'CN25', 'CN26', 'CN27', 'CN28', 'CN29', 'CN30', 'CN31', 'CN32', 'CN33', 'CN34', 'CN35', 'CN36', 'CN37', 'CN38', 'CN39', 'CN40', 'CN41', 'CN42', 'CN43', 'CN44', 'CN45']
BINLISTM=['CN1', 'CN2', 'CN3', 'CN4', 'CN5', 'CN6', 'CN7', 'CN8', 'CN9', 'CN10', 'CN11', 'CN12', 'CN13', 'CN14', 'CN15', 'CN16', 'CN17', 'CN18', 'CN19', 'CN20', 'CN21', 'CN22', 'CN23', 'CN24', 'CN25', 'CN26', 'CN27', 'CN28', 'CN29', 'CN30', 'CN31', 'CN32', 'CN33', 'CN34', 'CN35', 'CN36', 'CN37', 'CN38', 'CN39', 'CN40', 'CN41', 'CN42', 'CN43', 'CN44', 'CN45']
    
FLNDICT={"mumbai" : "AB001", "kolkata" : "AB002"}
usedpid=[]

def plane_define(FLN):
    cur.execute("CREATE TABLE "+FLN+" (sno INT(3) PRIMARY KEY, pid VARCHAR(5),name VARCHAR (25), rw INT(2), clmn CHAR(1),age INT(3), gender CHAR(1),CONSTRAINT upid UNIQUE(pid))")
    for i in range (0,20):
        rw=(i%5)+1
        clmn=str(chr(65+(i//5)))
        SQL='INSERT '+FLN+' VALUES (%s,NULL,NULL,%s,"%s",NULL,NULL)'%(i+1,rw,clmn)
        cur.execute(SQL)
    for i in range (0,25):
        rw=(i%5)+6
        clmn=chr(65+(i//5)) 
        cur.execute('INSERT '+FLN+' VALUES (%s,NULL,NULL,%s,"%s",NULL,NULL)'%(i+21,rw,clmn))

    db.commit()


def seat_check(FLN,rw,clmn):
    swql='select * from '+FLN+' where rw=%s and clmn="%s"'%(rw,clmn)
    print(swql)
    cur.execute(swql)
    db.commit()
    entry=cur.fetchone()
    return(entry[2]==None)


def plane_seats(FLN):
    print("\t  A B C D ")
    for rew in range (1,6):
        print(rew,'\t| ',end='')
        for colmn in ('A','B','C','D'):
            sql="select * from "+FLN+" where clmn='%s' and rw=%s"%(colmn,rew)
            cur.execute(sql)
            db.commit()
            entry=cur.fetchone()
            
            if entry[2]==None:
                print('⨁',end=' ')
            else:
                print('⨂',end=' ')
        

        print(' |')

    print("\t|A B C D E |")
    for rew in range (6,11):
        print(rew,'\t|',end='')
        for colmn in ('A','B','C','D','E'):
            sql="select * from "+FLN+" where clmn='%s' and rw=%s"%(colmn,rew)
            cur.execute(sql)
            db.commit()
            entry=cur.fetchone()
            
            if entry[2]==None:
                print('⨁',end=' ')
            else:
                print('⨂',end=' ')
        

        print('|')


def book_seat(FLN):
    plane_seats(FLN)
    print("⨁ are open seats \n⨂ are blocked/reserved seats")
    while True:
        try:
            rw=int(input("row:"))
            clmn=(str(input("column:"))).upper()
            if str(str(rw)+clmn) not in BLS:
                raise Exception()
        except  Exception:
            print("Please enter valid seat")
            
        else:
            break   
    while True:    

        gen=str(str(FLN[4])+str(str(random.randint(0,9))+str(random.choice(['W','X','Y','Z'])))+str(str(random.randint(0,9))+str(random.randint(0,9))))
        while gen in usedpid:
            gen=str(str(FLN[4])+str(random.randrange(0,9))+str(random.choice(['W','X','Y','Z']))+str(random.randint(0,9))+str(random.randint(0,9)))
        usedpid.append(gen)
        pid=gen
        name=str(input('name:'))
        AGE=int(input("Enter your current age: "))

        print('please check inputs')

        break
    
            
    GENDER=["male","female","other"]
    GNDR=input("Enter your Gender: ")
    GNDR.lower()
    while GNDR not in GENDER:
        print(GENDER)
        GNDR=input("Enter gender from above list: ")
    GNDR.upper()
    swql=('update '+FLN+' set pid="%s" , name="%s" , age=%s , gender="%s" where rw=%s and clmn="%s";'%(pid,name,AGE,GNDR[0],rw,clmn))
    if seat_check(FLN,rw,clmn):
        cur.execute(swql)
        db.commit()
        print("Your Passenger ID is :",pid)
        time.sleep(5)
        
    else:
        print("seat booked already, please choose another seat")
        time.sleep(5)

def covid():#block B and D seats
    for i in FLNDICT.values():
        sql="update "+i+" set name='BLOCKED' where rw='B' and rw='D'"
        db.commit()
        cur.execute(sql)


def also_covid():#remove all the B and D seats
    while True:
        for i in BLS:
            if i[1] in ("B","D"):
                indx=BLSE.index(i)
                BLS.pop(indx)
                BINLISTK.pop(-1)
                BINLISTM.pop(-1)

        
        break








def Bookseat():
    BLS=["1A","1B","1C","1D","2A","2B","2C","2D","3A","3B","3C","3D","4A","4B","4C","4D","5A","5B","5C","5D","6A","6B","6C","6D","6E","7A","7B","7C","7D","7E","8A","8B","8C","8D","8E","9A","9B","9C","9D","9E","10A","10B","10C","10D","10E"]#seat layout for business

    bookloop=True
    print ("Flights to:")
    for i in FLNDICT.keys():
        print (i)
    DSTN=input("Enter your Destination city: ").lower()
    
    
    
    if DSTN=="kolkata":
        if len(BINLISTK)!=0:
            while bookloop:
                book_seat(FLNDICT[DSTN])
                bookloop=False
            BINLISTK.pop(0)
        else:
            print('all seats booked')

    elif DSTN=="mumbai":    
        if len(BINLISTM)!=0:
            while bookloop:
                book_seat(FLNDICT[DSTN])
                bookloop=False
            BINLISTM.pop(0)
        else:
            print('all seats booked')
    else:
        print("no flights to that destination")
        pass


def Changeseat():
    BLS=["1A","1B","1C","1D","2A","2B","2C","2D","3A","3B","3C","3D","4A","4B","4C","4D","5A","5B","5C","5D","6A","6B","6C","6D","6E","7A","7B","7C","7D","7E","8A","8B","8C","8D","8E","9A","9B","9C","9D","9E","10A","10B","10C","10D","10E"]#seat layout for business

    bookloop=True
    print ("Flights to:")
    for i in FLNDICT.keys():
        print (i)
    DSTN=input("Enter your Destination city: ").lower()
    FLN=FLNDICT[DSTN]
    while bookloop:
        plane_seats(FLN)
        print("⨁ are open seats \n⨂ are blocked/reserved seats")
        while True:
            while True:    
                try:
                    pid=str(input("Enter your Passenger ID :"))
                    name=str(input('name:'))
                    AGE=int(input("Enter your current age: "))
                except (TypeError,ValueError):
                    print('please check inputs')
                else:
                    break
            while True:
                swql="select* from "+FLN+" where pid='%s' and name='%s'"%(pid,name)
                cur.execute(swql)
                db.commit()
                stuff=cur.fetchone()
                if stuff==None:
                    print("please enter valid name/Passenger ID")
                else:
                    break
            break
        print()

        swql="update "+FLN+" set pid=NULL, name=NULL, age=NULL, gender=NULL where pid='%s'"%(pid)
        cur.execute(swql)
        
        db.commit()
        while True:
            try:
                rw=int(input("row:"))
                clmn=(str(input("column:"))).upper()
                if str(str(rw)+clmn) not in BLS:
                    raise Exception()
            except  Exception:
                print("Please enter valid seat")
                
            else:
                break 

        GENDER=["male","female","other"]
        GNDR=input("Enter your Gender: ")
        GNDR.lower()
        while GNDR not in GENDER:
            print(GENDER)
            GNDR=input("Enter gender from above list: ")
        GNDR.upper()
        swql=('update '+FLN+' set pid="%s" , name="%s" , age=%s , gender="%s" where rw=%s and clmn="%s";'%(pid,name,AGE,GNDR[0],rw,clmn))
        print(swql)
        if seat_check(FLN,rw,clmn):
            cur.execute(swql)
            db.commit()
            print("Seat changed to :",rw,clmn)
            bookloop=False
        else:
            print("seat booked already, please choose another seat")


def Deleteseat():
    print ("Flights to:")
    for i in FLNDICT.keys():
        print (i)
    DSTN=input("Enter your Destination city: ").lower()
    FLN=FLNDICT[DSTN]
    while True:
        while True:    
            try:
                pid=str(input("Enter your Passenger ID :"))
                name=str(input('name:'))
                AGE=int(input("Enter your current age: "))
            except (TypeError,ValueError):
                print('please check inputs')
            else:
                break
        try:
            swql="select * from "+FLN+" where pid='%s'"%(pid)
            cur.execute(swql)
            db.commit() 

            row_count=cur.fetchone()
            if row_count==None:
                raise Exception   
        except Exception:
            print("invalid Name/Passenger ID \nPlease enter valid details")
        else:
            swql="update "+FLN+" set pid=NULL, name=NULL, age=NULL, gender=NULL where pid='%s'"%(pid)
            cur.execute(swql)
            db.commit() 
            print("Cancellation executed")
            if DSTN=='mumbai':
                BINLISTM.append("doesn't matter what it's called")
            if DSTN=='kolkata':
                BINLISTK.append("doesn't matter what it's called")
            break



def view_booking():
    print ("Flights to:")
    for i in FLNDICT.keys():
        print (i)
    DSTN=input("Enter your Destination city: ").lower()
    FLN=FLNDICT[DSTN]
    swql="select * from "+FLN
    cur.execute(swql)
    r=cur.fetchall()
    for sno,pid,name,rw,clmn,age,gender in r:
        if name==None:
            name='NULL'
        print("%3d | %5s | %25s | %2d | %s | %s | %s"%(sno,pid,name.ljust(25,'_'),rw,clmn,age,gender))    

exist=input("do tables exist?(Y/N):").upper()
if exist=='N':
    for i in FLNDICT.values():
        plane_define(i)

COVID=input("Do you live in covid times?(Y/N)")
if COVID=="Y":
    covid()
    also_covid()


while True:
    print("Options are:")
    print("B:Book seat")
    print('C:Change seat')
    print('D:Delete seat')
    print('V:View bookings')
    option=input("Choose option:").upper()
    if option=='B':
        Bookseat()
    elif option=='D':
        Deleteseat()
    elif option=='C':
        Changeseat()
    elif option=='V':
        view_booking()
    
