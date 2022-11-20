import pymysql
con=pymysql.connect(host='bpb77dvenawwog30sezn-mysql.services.clever-cloud.com',user='ukwqraqdm2ilww8w',password='8SUXQOa98uZs1RbAwUBr',database='bpb77dvenawwog30sezn') 
curs=con.cursor() 
com=input("Enter Company Name: ")
curs.execute("select company,modelname,price from MOBILES WHERE COMPANY='%s'ORDER BY price ASC"%com)
#curs.execute("select price from MOBILES ORDER BY price ASC")
Data=curs.fetchall()
print(Data)

con.close()
    