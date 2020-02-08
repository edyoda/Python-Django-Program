from db import *

class YoungerProfile():
    def __init__(self, email, password):
        self.email = email
        self.password = password
        sql = f'SELECT PK_user_id, name FROM users WHERE email = "{self.email}" '
        mycursor.execute(sql)
        user_id = mycursor.fetchone()
        self.user_id = user_id[0]
        self.younger_name = user_id[1]
        sql = f'SELECT PK_younger_id FROM youngers WHERE FK_user_id={self.user_id}'
        mycursor.execute(sql)
        younger_id = mycursor.fetchone()
        self.younger_id=younger_id[0]
        sql = f'SELECT FK_younger_id from elders where FK_younger_id = {self.younger_id}'
        mycursor.execute(sql)
        self.youngerCount = mycursor.fetchall()

    def sign_up(self, user_id):
        sql = "INSERT INTO youngers (FK_user_ID) VALUES (%s)"
        val = (user_id)
        mycursor.execute(sql, val)
        print("inserted")
        mydb.commit()

    def log_in(self):
        #retrieving passwords for registered mobile no from both table
        sql = f'SELECT password FROM users WHERE email= "{self.email}" '
        mycursor.execute(sql)
        user_info = mycursor.fetchone()     # fetchall provides empty list if record does not exists
        if user_info==[]:
            print(f'{self.email} ot registered. Please try to register first')
            import index      # due to mutual importing we are importing here just before method calling
        elif self.password==user_info[0]:
            print("Logged IN")
            self.dashboard_younger()
        else:
            print("Wrong email and password")
            import index

    def dashboard_younger(self):
        elderCount = len(self.youngerCount)
        print(f'Currentlty you are taking care of {elderCount} Elders\nYou can request for {4-elderCount} more elders to take care of.\n1.View list of Available elders to take care of.\n2.Give review and rating for a elder\n3.LogOut')
        choice = int(input())
        if choice==1:
            self.request_elder()
        elif choice==2:
            self.review()
        elif choice==3:
            self.log_out()

    # user should be able to see list of available elder and sent them request. NOTE:- 1 user can't sent request to same elder twice
    def request_elder(self):
        pass

    # younger can give rating and rating to elders
    def review(self):
        pass

    def log_out(self):
        import index