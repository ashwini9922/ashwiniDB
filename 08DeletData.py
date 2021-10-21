import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='volkswagen',database='bookstoredb')
curs=con.cursor()

try:
    Bcode=int(input("Enter BookCode : "))
    curs.execute("select * from books where BookCode=%d"%Bcode)
    data=curs.fetchone()
    print('BookName = %s'%data[1])
    print('Category = %s'%data[2])
    print('Author = %s'%data[3])
    print('Publication = %s'%data[4])
    print('edition = %s'%data[5])
    print('Price = %.2f'%data[6])
    print('page = %s'%data[7])

    l=input("Do you want to delete the book : ")
    if data:
        if l.upper()=='YES':
            curs.execute("delete from books where BookCode=%d"%Bcode)
            con.commit()
            print("Book deleted successfully")
        else:
            print("Ok;No Problem!")
except:
    print("Invalid data or code not exist")    
con.close()    