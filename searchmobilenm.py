import pymysql
con=pymysql.connect(host='bpb77dvenawwog30sezn-mysql.services.clever-cloud.com',user='ukwqraqdm2ilww8w',password='8SUXQOa98uZs1RbAwUBr',database='bpb77dvenawwog30sezn') 
curs=con.cursor()

mn=input("Enter model name: ") 

curs.execute("select modelname from MOBILES where modelname='%s'"%mn)
print("Mobile Name")
curs.execute("select company from MOBILES where modelname='%s'"%mn)
Data=curs.fetchall()
for i in Data:
    print(Data)

    
if Data:
    print("Mobile Details")
    curs.execute("select * from MOBILES")
    Data=curs.fetchall()
    print(Data)
else:
    print('Not found')
con.close()
