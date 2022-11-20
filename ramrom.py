import pymysql
con=pymysql.connect(host='bpb77dvenawwog30sezn-mysql.services.clever-cloud.com',user='ukwqraqdm2ilww8w',password='8SUXQOa98uZs1RbAwUBr',database='bpb77dvenawwog30sezn') 
curs=con.cursor()
rm=input("Enter RAM size: ") 
ro=input("Enter ROM size: ") 
curs.execute("select ram='%s',rom='%s' from MOBILES"%(rm,ro))
data=curs.fetchone()
if data:
    curs.execute("select company from MOBILES where ram='%s' AND rom='%s'"%(rm,ro))
    data=curs.fetchall()
    con.commit()
    print(data)
else:
    print("not found")