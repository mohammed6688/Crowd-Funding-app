import Project.createProject as cp
import Project.editProject as ep
import Project.deleteProject as dp


def viewProject():
    try:
        projects_read = open("projects.txt", "r")
        i = 0
        for project in projects_read:
            info = project.split('|')
            i += 1
            print(f"Project no.{i}\nTitle: {info[2]}\nDetails: {info[3]}\nTotal target: {info[4]}\n"
                  f"Start date: {info[5]}\n"
                  f"End date: {info[6]}\n")
    except Exception as e:
        print(f"error while reading projects file: {e}")





def listOptions(userid: int):
    value = input("Choose on option:\n1)Create a project"
                  "\n2)View a project\n3)Delete a project\n4)Edit a project\n5)LogOut\n")
    if value.isdigit():
        if int(value) == 1:
            cp.createProject(userid)
            listOptions(userid)
        elif int(value) == 2:
            viewProject()
            listOptions(userid)
        elif int(value) == 3:
            dp.deleteProject(userid)
            listOptions(userid)
            pass
        elif int(value) == 4:
            ep.editProject(userid)
            listOptions(userid)
            pass
        elif int(value) == 5:
            pass
        else:
            print("you entered a wrong number")
            listOptions(userid)
    else:
        print("you entered wrong value")
        listOptions(userid)
