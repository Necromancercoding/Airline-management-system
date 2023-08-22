import pymysql

db=pymysql.connect(host="localhost", user="root", password="raikkonenrox123", db="Airseatbooking")
MyCur=db.cursor()
ECOLUMNS=["A","B","C","D","E"]#you decide if you need these or not
BCOLUMNS=["A","B","C","D"]#you decide if you need these or not
BLSE=["1A","1B","1C","1D","1E","2A","2B","2C","2D","2E","3A","3B","3C","3D","3E","4A","4B","4C","4D","5E","5A","5B","5C","5D","5E"]#seat layout for economy
BLSB=["1A","1B","1C","1D","2A","2B","2C","2D","3A","3B","3C","3D","4A","4B","4C","4D","5A","5B","5C","5D"]#seat layout for business
BLSEK=BLSE#Kolkata Economy, you decide if you need these or not
BLSBK=BLSB#Kolkata Business, you decide if you need these or not
BLSEM=BLSE#Mumbai Economy, you decide if you need these or not
BLSBM=BLSB#Mumbai Business, you decide if you need these or not
BINLISTK=['CN1', 'CN2', 'CN3', 'CN4', 'CN5', 'CN6', 'CN7', 'CN8', 'CN9', 'CN10', 'CN11', 'CN12', 'CN13', 'CN14', 'CN15', 'CN16', 'CN17', 'CN18', 'CN19', 'CN20', 'CN21', 'CN22', 'CN23', 'CN24', 'CN25', 'CN26', 'CN27', 'CN28', 'CN29', 'CN30', 'CN31', 'CN32', 'CN33', 'CN34', 'CN35', 'CN36', 'CN37', 'CN38', 'CN39', 'CN40', 'CN41', 'CN42', 'CN43', 'CN44', 'CN45']
BINLISTM=['CN1', 'CN2', 'CN3', 'CN4', 'CN5', 'CN6', 'CN7', 'CN8', 'CN9', 'CN10', 'CN11', 'CN12', 'CN13', 'CN14', 'CN15', 'CN16', 'CN17', 'CN18', 'CN19', 'CN20', 'CN21', 'CN22', 'CN23', 'CN24', 'CN25', 'CN26', 'CN27', 'CN28', 'CN29', 'CN30', 'CN31', 'CN32', 'CN33', 'CN34', 'CN35', 'CN36', 'CN37', 'CN38', 'CN39', 'CN40', 'CN41', 'CN42', 'CN43', 'CN44', 'CN45']
BIN=""
FLN=""
PNM=""
AGE=""
SR=""
SC=""
def Bookseat():
    DSTN=input("Enter your Destination city: ")
    if DSTN=="Kolkata":    
        BIN=BINLISTK[0]
        MyCur.execute("insert into Kolkata(BIN_No) values ("+str(BIN)+")")
        db.commit()
        PNM=input("Enter your full name")
        AGE=int(input("Enter your current age: "))
        GENDER=["male","female","other"]
        GNDR=input("Enter your Gender: ")
        GNDR.lower()
        while GNDR not in GENDER:
            print(GENDER)
            GNDR=input("Enter gender from above list: ")
        print("")
        MyCur.execute("insert into "+str(DSTN)+"(Bin_No,Passenger_Name,Age,Gender) values("+str(BINLISTK)+","+str(PNM)+","+str(AGE)+","+str(GNDR)+") where Bin_No="+str(BIN))
        db.commit()
        BINLISTK.remove[0]
        COVID=input("Do you live in covid times?(Y/N)")
        if COVID=="Y":
            SR=input("Enter your chosen seat row number: ")
            SC=input("Enter your chosen seat column alphabet: ")
            
        if COVID=="N":
            SR=input("Enter your chosen seat row number: ")
            SC=input("ENter your chosen seat column alphabet: ")

    if DSTN=="Mumbai":    
        BIN=BINLISTM[0]
        MyCur.execute("insert into Mumbai(BIN_No) values ("+str(BIN)+")")
        db.commit()
        PNM=input("Enter your full name")
        AGE=int(input("Enter your current age: "))
        GENDER=["male","female","other"]
        GNDR=input("Enter your Gender: ")
        GNDR.lower()
        while GNDR not in GENDER:
            print(GENDER)
            GNDR=input("Enter gender from above list: ")
        print("")
        MyCur.execute("insert into "+str(DSTN)+"(Bin_No,Passenger_Name,Age,Gender) values("+str(BINLISTM)+","+str(PNM)+","+str(AGE)+","+str(GNDR)+") where Bin_No="+str(BIN))
        db.commit()
        BINLISTM.remove[0]
        COVID=input("Do you live in covid times?(Y/N)")
        if COVID=="Y":
            SR=input("Enter your chosen seat row number: ")
            SC=input("Enter your chosen seat column alphabet: ")
            
        if COVID=="N":
            SR=input("Enter your chosen seat row number: ")
            SC=input("ENter your chosen seat column alphabet: ")

def Changeseat():
    BIN=input("Enter your BIN number: ")
    PNM=input("Enter your full name: ")
    DSTN=input("Enter your destination city: ")
    SR=input("Enter your new chosen seat row number: ")
    SC=input("ENter your new chosen seat column letter: ")
    MyCur.execute("Update "+str(DSTN)+" set Seat_Row = "+str(SR)+" where Bin_No="+str(BIN)+" and Passenger_Name="+str(PNM))
    db.commit()
    print("Your seat number has been succesfully changed.")

def Deleteseat():
    BIN=input("Enter your BIN number: ")
    PNM=input("Enter your full name: ")
    DSTN=input("Enter Destination city: ")
    SR=input("Enter your current chosen seat row number: ")
    SC=input("ENter your current chosen seat column letter: ")
    MyCur.execute("Delete from "+str(DSTN)+" where Bin_No="+str(BIN))
    db.commit()
    print("Cancellation executed")





            
        
    


