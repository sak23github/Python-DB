import pymysql
try:
    prodid=int(input('Enter product id: '))
    mn=input("Enter model name: ")
    com=input("Enter company name: ")
    conn=input("Enter connectivity(4G/5G): ") 
    ram=input("Enter Ram Size: ") 
    rom=input("Enter Rom size: ")
    color=input("Enter colour: ")
    scr=input("Enter screen type: ")
    batt=input("Enter battery capacity:")
    proc=input("Enter processor Name: ")
    price=int(input("Enter price: "))
    rating=float(input("Enter rating of mobile(out 0f 5): ")) 
    con=pymysql.connect(host='bpb77dvenawwog30sezn-mysql.services.clever-cloud.com',user='ukwqraqdm2ilww8w',password='8SUXQOa98uZs1RbAwUBr',database='bpb77dvenawwog30sezn') 
    curs=con.cursor()  
    
    curs.execute("insert into MOBILES values( %d,'%s','%s','%s','%s','%s','%s','%s','%s','%s',%d,%.2f)" %(prodid,mn,com,conn,ram,rom,color,scr,batt,proc,price,rating))
    con.commit()
    print("New Customer registred successfully: ")
    con.close()
except Exception as e:
    print("Can't register: ,e")