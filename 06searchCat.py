import mysql.connector as mycon
con=mycon.connect(host='localhost',user='root',password='volkswagen',database='bookstoredb')
curs=con.cursor()

cat=input('Enter the category : ')
curs.execute("select bookname from books where Category='%s'"%cat)
data=curs.fetchall()
books=[]

for rec in data:
    books.append(rec[0])
    
print(books)