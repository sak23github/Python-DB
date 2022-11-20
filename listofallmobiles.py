import pymysql

con=pymysql.connect(host='bpb77dvenawwog30sezn-mysql.services.clever-cloud.com',user='ukwqraqdm2ilww8w',password='8SUXQOa98uZs1RbAwUBr',database='bpb77dvenawwog30sezn') 
curs=con.cursor()  
curs.execute("select company from MOBILES")
company=curs.fetchone()
while company:
  print(company)
  company=curs.fetchone()
print("YUP..!HERE IS THE LIST OF ALL MOBILES ")
    
