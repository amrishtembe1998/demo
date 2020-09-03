import mysql.connector as connector
import pandas as pd
db_connection = connector.connect(host='localhost', database='pythontest', user='root', password='root')
db_cursor = db_connection.cursor()
class DBHelper:
        #Creating a constructor to create the connection and then query to add table in the database
    def __init__(self):
        self.con = connector.connect(host='localhost',
                        port='3306',
                        database='pythontest',
                        password='root',
                        user='root')
        query = 'create table if not exists user (userId int primary key, userName varchar(200), phone varchar(12))'
        cur = self.con.cursor()
        cur.execute(query)
        
        #Insert records into the table
    def insert_user(self,userid,username,phone):
        query = "insert into user(userId, userName, phone) values({},'{}','{}')".format(userid,username,phone)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user saved to database")
        
        #Fetch all the records from table
    def fetch_all(self):
        query = 'select * from user'
        cur = self.con.cursor()
        cur.execute(query)
        data = cur.fetchall()
        df = pd.DataFrame(data, columns=['User ID','User Name','Phone'])
        df.index = df.index + 1
        print(df)
        print("This is all we have")
        
        #Fetch record of selected ID
    def fetch_one(self,id):
        query = 'select * from user where userId={}'.format(id)
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print(row)
        print('done')

        #Delete user from the table with selected ID
    def delete_user(self,userId):
        query = 'delete from user where userId={}'.format(userId)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Deleted")
    
        #Update the records with the help of User ID
    def update_user(self,userId,newName,newPhone):
        query = "update user set userName='{}', phone='{}' where userId={}".format(newName,newPhone,userId)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('updated')

        