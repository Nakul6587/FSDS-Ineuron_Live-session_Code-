
import mysql.connector
# Connect to the database
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="654321",
)

cur = mydb.cursor()

#to create the data base use below one line code but if you ant to add anothweer code remark this code so it won't executer again and not shows an erro

#cur.execute('create database new_fsds_db')

cur.execute('use new_fsds_db')

#cur.execute('create table fsds1 (name varchar(40), roll_no int, mail_id varchar(30)) ')

cur.execute ("insert into fsds1 values ('sudhanshu', 3534, 'nakul6587@gmail.com')")

mydb.commit()
