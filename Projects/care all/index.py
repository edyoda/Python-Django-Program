from db import *
from profile import User
from younger_profile import YoungerProfile
from elder_profile import ElderProfile

# welcome note and giving oprion to login or register
def welcome():
    print("Please select\n1. Login as Elder \n2. Login as Younger\n3. Register\n4. View all youngers who are taking care\n5. View who is taking care of older couple\n6. Exit")
    task = int(input())
    if task==1:
        mobile = input("Welcome Elder\nEnter Your Email: ")
        password = input("Enter Your Password: ")
        user = ElderProfile(mobile, password)
        user.log_in()
    
    elif task==2:
        mobile = input("Welcome younger\nEnter Your Email: ")
        password = input("Enter Your Password: ")
        user = YoungerProfile(mobile, password)
        user.log_in()
    
    elif task==3:
        name = input("Register Yourself\nEnter Your Full Name: ")
        email = input("Enter your email: ")
        mobile = input("Enter Your Mobile Number: ")
        password = input("Enter Your Password: ")
        
        # if a user select wrong option it will ask again to select option
        while True:
            role = int(input("select your role:\n1. Elder\n2. Younger\n"))
            try:
                if role==1:
                    role="elder"
                    break
                elif role==2:
                    role="younger"
                    break
            except:
                print(f'option not Valid! Please try again')

        user_signup = User(name, email, password, mobile, role)
        user_signup.user_registration()
        
    # display name of youngers who are taking care of
    elif task==4:
        pass

    # enter elder's mobile number of email boh are unique here and display their take care name
    elif task==5:
        pass

    elif task==6:
        exit()

welcome()
