import pymysql
import logging
# setting logging config
logging.basicConfig(filename="question8.log", 
                    format='%(asctime)s %(message)s', 
                    filemode='w') 
logger=logging.getLogger()
logger.setLevel(logging.ERROR) 

dbServerName    = "kishandb1.csaruqlxxway.us-east-1.rds.amazonaws.com"

dbUser          = "kishan"

dbPassword      = "kishan123"

dbName          = "kishan123"

con = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword, db=dbName, port=3306)


#creating table Games12
try:
    create = "CREATE TABLE Games12(gid int, gname varchar(20), rating int, date varchar(15))"
    cur = con.cursor()
    cur.execute(create)
    show_tables = "show tables"
    cur.execute(show_tables)
    rows = cur.fetchall()
    for i in rows:
        print(i)
except Exception as e:
    logger.error(e) 
    print('error occured please check your code ')

    
#inserting into table values
try:
    insert = "INSERT INTO Games12(gid, gname,rating,date) VALUES (1, 'football',10,'1/4/19'),(2, 'basketball',9,'6/06/19'),(3, 'volleyball',8,'2/7/19')"
    cur.execute(insert)
    cur.commit()
except Exception as e:
    logger.error(e) 
    print('error occured please check your code ')#update the table
try:
    update = "UPDATE Games12 SET gname = cricket WHERE gid = 1"
    cur.execute(update)
    cur.commit()
    
except Exception as e:
    logger.error(e) 
    print('error occured please check your code ')


#read the table
try:

    read = "SELECT * FROM Emp"
    cur.execute(read)
    rows = cur.fetchall()
    for row in rows:
        print(row)
except Exception as e:
    logger.error(e) 
    print('error occured please check your code ')


#deleting a column
try:
    delete = "DELETE FROM Emp WHERE gid = 1"

    cur.execute(delete)
    cur.commit()
except Exception as e:
    logger.error(e) 
    print('error occured please check your code ')
    
#closing the connection
finally:
    con.close()


