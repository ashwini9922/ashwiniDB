import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='volkswagen',database='bookstoredb')
curs=con.cursor()

no=int(input("Enter the bookcode : "))
curs.execute("select bookname,category,Author,Publication ,edition,Price,page from books where bookcode=%d"%no)
rec=curs.fetchone()

try:
    print('BookName = %s'%rec[0])
    print('Category = %s'%rec[1])
    print('Author = %s'%rec[2])
    print('Publication = %s'%rec[3])
    print('edition = %s'%rec[4])
    print('Price = %.2f'%rec[5])
    print('page = %s'%rec[6])
except:
    print('Book does not found.')    
con.close()
