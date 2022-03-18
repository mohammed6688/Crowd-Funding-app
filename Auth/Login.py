import re
import Project.userOptions as userOptions

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
user_info = []


def loginUser():
    userEmail()
    userPassword()
    checkUser()


def userEmail():
    email = input("enter your email\n")
    if re.fullmatch(regex, email):
        user_info.insert(len(user_info), email)
    else:
        print("you entered wrong email format\n")
        userEmail()


def userPassword():
    user_pass = input("enter your password\n")
    if any(i.isdigit() for i in user_pass):
        user_info.insert(len(user_info), user_pass)
    else:
        print("you entered wrong password\n")
        userPassword()


def checkUser():
    try:
        users_read = open("users.txt", "r")
        for user in users_read:
            info = user.split('|')
            if info[3] == user_info[0] and info[4] == user_info[1]:
                userOptions.listOptions(info[0])
        else:
            print("there is no user with that credentials")

    except Exception as e:
        print(e)