import pymysql
try:
    mn=input("Enter Model Name: ")
    pur=input("Enter purpose: ")
    con=pymysql.connect(host='bpb77dvenawwog30sezn-mysql.services.clever-cloud.com',user='ukwqraqdm2ilww8w',password='8SUXQOa98uZs1RbAwUBr',database='bpb77dvenawwog30sezn') 
    curs=con.cursor()
    curs.execute("update MOBILES set modelname='%s' where purpose='%s'"%(mn,pur))
    data=curs.fetchall()
    con.commit()
    con.close()
    print("updated succesfully")
except:
    print("Enter valid input: ")
    