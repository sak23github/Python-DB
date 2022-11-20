import pymysql
try:
    proid=int(input("Enter product id: "))
    con=pymysql.connect(host='bpb77dvenawwog30sezn-mysql.services.clever-cloud.com',user='ukwqraqdm2ilww8w',password='8SUXQOa98uZs1RbAwUBr',database='bpb77dvenawwog30sezn') 
    curs=con.cursor()
    curs.execute("select * from MOBILES where prodid=%d" %proid)
    data=curs.fetchone()

    if data:
        print(data)
        cho=input('Do you really want to delete? (yes/no) : ')
        if cho.upper()=='YES':
            curs.execute("delete from MOBILES where prodid=%d" %proid)
            con.commit()
            print('Data deleted')
        else:
            print('Delete operation cancelled')
    else:
        print('Enter valid product id')

    con.close()
except:
    print('failed')