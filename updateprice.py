import pymysql
try:
 proid=int(input("Enter product id: "))
 np=int(input("Enter new price: "))
 con=pymysql.connect(host='bpb77dvenawwog30sezn-mysql.services.clever-cloud.com',user='ukwqraqdm2ilww8w',password='8SUXQOa98uZs1RbAwUBr',database='bpb77dvenawwog30sezn') 
 curs=con.cursor()
 curs.execute("select * from MOBILES where prodid=%d" %proid)
 data=curs.fetchone()

 if data:
     curs.execute("update MOBILES set price=%d where prodid=%d"%(np,proid))
     con.commit()
     print("price is updated")
 else:
    print('Mobile does not exist')
    con.close()
except:
    print('failed')


