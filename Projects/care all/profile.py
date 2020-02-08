from db import *
from younger_profile import YoungerProfile
from elder_profile import ElderProfile

# user registration class
class User:
    #constructors
    def __init__(self, name, email, password, mobile, role):
        self.name = name
        self.email = email
        self.password = password
        self.mobile = mobile
        self.role = role
        

    def user_registration(self):
        #retrieving all registered email no from user table
        user_id = self.get_user_id()
        
        if user_id is None:
            sql = "INSERT INTO users (name, email, password, mobile) VALUES (%s, %s, %s, %s)"
            val = (self.name, self.email, self.password, self.mobile)
            mycursor.execute(sql, val)
            mydb.commit()  

        # if email already registered ask them to login again or reset password
        else:
            print(f'Account already created for {self.email} Please try to Login using your mobile number and password.\n Want to reset password?\n1. Yes\n2. No')
            reset_pass = int(input())
            # Reset password Function
            if reset_pass==1:
                new_pass = input("Enter your New pass: ")
                sql = "UPDATE users set password = %s WHERE email = %s"
                val = ( new_pass, self.email)
                mycursor.execute(sql, val)
                mydb.commit()
                print("Password Reset Successfully.")  
            else:
                import index    # due to mutual importing we are importing here just before methodcalling

        if self.role=="younger":
            younger = YoungerProfile(self.email, self.password)
            younger.sign_up(self.get_user_id())
        elif self.role=="younger":
            elder = ElderProfile(self.email, self.password)
            elder.sign_up(self.get_user_id())

    def get_user_id(self):
        sql = f'SELECT PK_user_id FROM users WHERE email = "{self.email}" '
        mycursor.execute(sql)
        user_id = mycursor.fetchone()
        return user_id

