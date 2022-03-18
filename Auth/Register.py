import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
user_info = []


def registerUser():
    firstName()
    lastName()
    email()
    password()
    phone()
    addUser()
    print(user_info)


def addUser():
    try:
        user_write = open("users.txt", "a")
        users_read = open("users.txt", "r")
        max_id = len(users_read.readlines())
        user_write.write(
            str(int(max_id) + 1) + "|" + str(user_info[0]) + "|" + user_info[1] + "|" + user_info[2] + "|"
            + user_info[3] + "|" + user_info[4] + "\n")
    except Exception as e:
        print(f"error while write register file: {e}")
    # main.viewMainOptions()


def firstName():
    first_name = input("enter your first name\n")
    if all(not i.isdigit() for i in first_name):
        user_info.insert(len(user_info), first_name)
    else:
        print("you entered wrong name\n")
        firstName()


def lastName():
    last_name = input("enter your last name\n")
    if all(not i.isdigit() for i in last_name):
        user_info.insert(len(user_info), last_name)
    else:
        print("you entered wrong name\n")
        lastName()


def email():
    em = input("enter your email\n")
    if re.fullmatch(regex, em):
        user_info.insert(len(user_info), em)
    else:
        print("you entered wrong email format\n")
        email()


def password():
    user_password = input("enter your password\n")
    if any(i.isdigit() for i in user_password):
        con_password = input("enter your password again\n")
        if any(i.isdigit() for i in con_password) and user_password == con_password:
            user_info.insert(len(user_info), con_password)
        else:
            print("you entered wrong password\n")
            password()
    else:
        print("you entered wrong password format\n")
        password()


def phone():
    user_phone = input("enter your phone number\n")
    if len(user_phone) == 11:
        user_info.insert(len(user_info), user_phone)
    else:
        print("you entered wrong phone number\n")
        phone()
