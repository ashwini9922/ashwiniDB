import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='volkswagen',database='bookstoredb')
curs=con.cursor()

try:
    Bcode=int(input('Enter book code :  '))
    Bnm=input('Enter book name :  ')
    cat=input('Enter Type of category :  ')
    Athr=input('Enter Author Name :  ')
    pr=input('Enter publication :  ')
    Ed=input('Enter Edition : ')
    prc=float(input('Enter Price :  '))  
    pg=int(input('Enter pages :  '))

    curs.execute("insert into books values(%d,'%s','%s','%s','%s','%s',%.2f,%d)" %(Bcode,Bnm,cat,Athr,pr,Ed,prc,pg))
    con.commit()
    print('Book added successfully')
    
except:
    print('cant take data..invalid input')

con.close()
