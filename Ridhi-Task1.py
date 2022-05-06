import json
import os
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def initiate_process():
    choice = int(input("Please enter 1 for Registration, 2 for Login: "))
    print(choice)
    if choice ==1:
        register_new_user()
    elif choice ==2:
        login_user()
    else:
        initiate_process()

def register_new_user():
    user_name = input("Please enter a valid email/username to login: ")
    if not validate_user_email(user_name):
        register_new_user()
    else:
        add_password_to_user(user_name)

def login_user():
    user_name = input("Please enter your user name: ")
    password = input("Please enter your password: ")
    if is_valid_user_name(user_name):
        if match_user_password(user_name, password):
            print("Congrats you are a valid user!!!!")
            initiate_process()
        else:
          action = int(input("Your password did not match, type '1' for forgotten the password and '2' for registration "))
          if action ==1:
            forgot_password(user_name)
          else:
            register_new_user()
    else:
        user_name = input("OOps are you a hakcker, press any key to continue***")
        login_user()

def forgot_password(user_name):
    file_name = "datastore.json"
    with open(file_name, 'r') as f:
        data = json.load(f)
        for user in data["user_data"]:
            if user['user_name'] == user_name:
                action = input("Your password for username :"+user_name + " is "+user['password'])
                login_user()

def is_valid_user_name(user_name):
    file_name = "datastore.json"
    with open(file_name, 'r') as f:
        data = json.load(f)
        return find_the_user(user_name,data['user_data'])

def match_user_password(user_name, password):
    file_name = "datastore.json"
    with open(file_name, 'r') as f:
        data = json.load(f)
        for user in data["user_data"]:
            if user['user_name'] == user_name and user['password'] ==password:
                return True
        return False

def find_the_user(user_name,listOfUsers):
    for user in listOfUsers:
        if user['user_name'] == user_name:
            return True
    return False;


def add_password_to_user(user_name):
    password = input("Please enter a password for the username: ")
    if validate_password(password):
        save_user_details_to_file(user_name,password)
    else:
        add_password_to_user(user_name)

def save_user_details_to_file(user_name,password):
    file_name = "datastore.json"
    with open(file_name, 'r') as f:
        data = json.load(f)
        data['user_data'].append({"user_name":user_name,"password":password});

    os.remove(file_name)
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=4)
    password = input("User saved username : "+user_name +"  -- password : "+ password )
    initiate_process()

def validate_user_email(user_name):
    if(re.fullmatch(regex, user_name)):
        return True
    else :
        return False


def validate_password(password):
    SpecialSym =['$', '@', '#', '%']
    val = True
      
    if len(password) < 6:
        print('length should be at least 6')
        val = False
          
    if len(password) > 16:
        print('length should not be greater than 16')
        val = False
          
    if not any(char.isdigit() for char in password):
        print('Password should have at least one numeral')
        val = False
          
    if not any(char.isupper() for char in password):
        print('Password should have at least one uppercase letter')
        val = False
          
    if not any(char.islower() for char in password):
        print('Password should have at least one lowercase letter')
        val = False
          
    if not any(char in SpecialSym for char in password):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return val

initiate_process()









        


        

