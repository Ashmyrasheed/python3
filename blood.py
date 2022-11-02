import mysql.connector

mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'bloodbankdb')
mycursor = mydb.cursor()
while True:

    print("select an option from the menu")

    print("1 add blood banker")

    print("2 view all blood banker")  

    print("3 search a blood banker")

    print("4 update the blood banker")    

    print("5 delete a blood banker")

    print("6 exit")

   

    choice = int(input('enter an option:'))

    if(choice==1):

        print('blood banker enter selected')
        
        
        

        nameofdonar = input('enter the name')

        phno = input('enter the phno')

        bloodgroup = input('enter the bloodgroup ')

        litreofblood = input('enter the litreofblood')
        
        
        
        sql = 'INSERT INTO `bloodbank`( `nameofdonar`, `phno`, `bloodgroup`, `litreofblood`) VALUES (%s,%s,%s,%s)'

        

        data = (nameofdonar,phno,bloodgroup,litreofblood)

        mycursor.execute(sql , data)

        mydb.commit()
        
        

    elif(choice==2):

        print('view blood banker')
        
        sql = 'SELECT * FROM `bloodbank`'
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)

        print('view book')
    elif(choice==3):

        print('search blood banker')
        
        bloodgroup = input('enter blood group')
        
        sql = "SELECT `id`,`nameofdonar`,`phno`,`bloodgroup`,`litreofblood` FROM `bloodbank` WHERE `bloodgroup` = '"+bloodgroup+"'"

        mycursor.execute(sql)

        result = mycursor.fetchall()

        print(result)

    elif(choice==4):

        print('update blood banker')
        
        
        bloodgroup = input('enter the bloodgroup')
        
        nameofdonar = input('enter the name')
        phno = input('enter the phno')
        bloodgroup = input('enter the bloodgroup')
        litreofblood = input('enter the litrofblood')
   
    
        
        sql = "UPDATE `bloodbank` SET `nameofdonar`='"+nameofdonar+"',`phno`='"+phno+"',`bloodgroup`='"+bloodgroup+"',`litreofblood`='"+litreofblood+"' WHERE `bloodgroup`='"+bloodgroup+"'"
    
        mycursor.execute(sql)
        mydb.commit()
        print("data updated succesfully")
    
    elif(choice==5):

        print('delete blood banker')
        
        bloodgroup = input('enter the bloodgroup')

        blood_group = input('enter the blood group to be deleting: ')

        sql = "DELETE FROM `bloodbank` WHERE `bloodgroup`='"+bloodgroup+"'"

        mycursor.execute(sql)

        mydb.commit()
        print("data deleted succesfully")


    elif(choice==6):

        break