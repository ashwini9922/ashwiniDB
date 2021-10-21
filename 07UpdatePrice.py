import mysql.connector as mycon
con=mycon.connect(host='localhost',user='root',password='volkswagen',database='bookstoredb')
curs=con.cursor()

try:
    Bcode=int(input("Enter BookCode : "))
    curs.execute("select * from books where BookCode=%d"%Bcode)
    data=curs.fetchall()

    if data:
        amt=float(input("Enter new price : "))
        curs.execute("update books set Price = %.2f"%amt)
        con.commit()
        print("price updated successfully")
    else:
        print("Book not found")
except:
    print("enter valid data")
con.close()