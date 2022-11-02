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

    elif(choice==4):

        print('update blood banker')

    elif(choice==5):

        print('delete blood banker')

    elif(choice==6):

        break