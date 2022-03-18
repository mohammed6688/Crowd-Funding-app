import Auth.Register as Register
import Auth.Login as Login


def viewMainOptions():
    value = input("Choose on option:\n1)Register\n2)Login\n")
    if value.isdigit():
        if int(value) == 1:
            Register.registerUser()
            viewMainOptions()
        elif int(value) == 2:
            Login.loginUser()
            viewMainOptions()
        else:
            print("you entered a wrong number")
            viewMainOptions()
    else:
        print("you entered wrong value")
        viewMainOptions()


viewMainOptions()
