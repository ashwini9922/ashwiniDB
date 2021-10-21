import mysql.connector

con=mysql.connector.connect(host='localhost',user='root',password='volkswagen',database='bookstoredb')
curs=con.cursor()

curs.execute("select * from books")
data=curs.fetchall()

print(data)
print('-'*50)

for rec in data:
    
    print(rec[1])

con.close()