import mysql.connector as sql

# connection = sql.connect(
#                 host = 'localhost',
#                 port = '3306',
#                 user = 'user1',
#                 password = 'password',
#                 database = 'learn_website'
#             )

class DBHELPER:
    def __init__(self):
        self.con = sql.connect(
                host = 'localhost',
                port = '3306',
                user = 'user1',
                password = 'password',
                database = 'oop_flask_and_mysql'
                )
        # create table if it doesnt exits   
        query = 'CREATE TABLE IF NOT EXISTS user(userid INT AUTO_INCREMENT PRIMARY KEY,username VARCHAR(200),email VARCHAR(200),phone VARCHAR(12))'
        curr = self.con.cursor()
        curr.execute(query)
        print("Created")

    # inserting in db
    def insert_user(self,username,email,phone):
        query = "INSERT INTO user(username,email,phone) VALUES('{}','{}',{})".format(username,email,phone)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('user saved to db')

    def fetch_all(self):
        query = "SELECT * FROM user"
        cur = self.con.cursor()
        cur.execute(query)
        dataset = cur.fetchall()
        return dataset
        # print('here are your datasets\n\n')
        # for row in dataset:
        #     print('ID: ',row[0])
        #     print('NAME: ',row[1])
        #     print('EMAIL: ',row[2])
        #     print("PHONE NO: ",row[3])
        #     print('\n\n')

    def delete_user(self,userid):
        query = 'DELETE FROM user WHERE userid = {}'.format(userid)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Userid {} deleted !".format(userid))

    def update_user(self,userid,new_name,new_email,new_phone):
        query = 'UPDATE user SET username="{}",email="{}",phone="{}" WHERE userid={}'.format(new_name,new_email,new_phone,userid)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Userid {} updated !".format(userid))
