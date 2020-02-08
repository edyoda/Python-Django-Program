from db import *

class ElderProfile():
    def __init__(self, email, password):
        self.email = email
        self.password = password
        sql = f'SELECT PK_user_id, name FROM users WHERE email = "{self.email}" '
        mycursor.execute(sql)
        user_id = mycursor.fetchone()
        self.user_id = user_id[0]
        self.elder_name = user_id[1]
        sql = f'SELECT PK_elder_id FROM elders WHERE FK_user_id={self.user_id}'
        mycursor.execute(sql)
        elder_id = mycursor.fetchone()
        self.elder_id=elder_id[0]

    def sign_up(self, user_id):
        sql = "INSERT INTO elders (FK_user_ID) VALUES (%s)"
        val = (self.user_id)
        mycursor.execute(sql, val)
        mydb.commit()

    def log_in(self):
        #retrieving passwords for registered mobile no from both table
        sql = f'SELECT password FROM users WHERE email= "{self.email}" '
        mycursor.execute(sql)
        user_info = mycursor.fetchone()     # fetchall provides empty list if record does not exists
        if user_info==[]:
            print(f'{self.email} not registered. Please try to register first')
            import index      # due to mutual importing we are importing here just before method calling
        elif self.password==user_info[0]:
            print("Logged IN")
            self.dashboard_elder()
        else:
            print("Wrong email and password")
            import index

    def dashboard_elder(self):
        sql = f'SELECT available FROM elders where PK_elder_id = {self.elder_id}'
        mycursor.execute(sql)
        user_info = mycursor.fetchone()
        if user_info[0]==1:
            print("You are currently Available to take care of.\n1.Make Unavailable\n2.Fund\n3.Request\n4.Take Care Name\n5.Give review and rating for a younger\n6.LogOut")
            choice = int(input())
            if choice==1:
                self.change_status()
                self.dashboard_elder()
            elif choice==2:
                self.allocate_fund()
            elif choice==3:
                self.show_request()
            elif choice==4:
                self.take_care_name()
            elif choice==5:
                self.review()
            elif choice==6:
                self.log_out()

        else:
            print("You are currently Unavailable to take care of.\n1.Make Available\n2.Log Out")
            choice = int(input())
            if choice==1:
                self.change_status()
                self.dashboard_elder()
            elif choice==2:
                self.log_out()

    # elder should be able to allocate fund
    def allocate_fund(self):
        pass

    # elder can change their status from available to unavailable and vice-versa
    def change_status(self):
        pass

    # elder can see requests and accept whome they trus only 1 request can be accepted by elder      
    def show_request(self):
        pass

    # elder can see name of younger who is taking care of them
    def take_care_name(self):
        pass

    # elder can give review and rating to youngers
    def review(self):
        pass

    def log_out(self):
        import index
