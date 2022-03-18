from datetime import datetime

projects_ids = []
all_projects = []
project_info = []
# project_info = ['3', '1', 'title ed', 'detail ed', '1000', '20-10-2022', '20-10-2022']
date_format = "%d-%m-%Y"


def editor(userid):
    value = input("select project to edit ")
    if not int(value) > len(projects_ids):
        project_info.clear()
        titleVal()
        detailsVal()
        targetVal()
        startDateVal()
        endDateVal()
        addProject(userid, int(value))
    else:
        print("you entered wrong choice")
        editor(userid)


def addProject(userid, project_id: int):
    try:
        projects_read = open("projects.txt", "r")
        i = 0
        for project in projects_read:
            i += 1
            info = project.split('|')
            if info[1] == projects_ids[project_id-1]:
                item = str(userid) + "|" + projects_ids[project_id-1] + "|" + str(project_info[0]) + "|" + project_info[
                    1] + "|" + project_info[2] + "|" + project_info[3] + "|" + project_info[4] + "\n"
                all_projects[i - 1] = item
                print("edited successfully")
                projects_write = open("projects.txt", "w")
                projects_write.writelines(all_projects)

    except Exception as e:
        print(f"error while write project file: {e}")


def editProject(userid):
    try:
        projects_read = open("projects.txt", "r")
        i = 0
        all_projects.clear()
        projects_ids.clear()
        for project in projects_read:
            all_projects.insert(len(all_projects), project)
            info = project.split('|')
            if info[0] == userid:
                i += 1
                print(f"{i})Title: {info[2]}")
                projects_ids.insert(len(projects_ids), info[1])
        if not len(projects_ids) == 0:
            editor(userid)
        else:
            print("you dont created projects yet")
    except Exception as e:
        print(f"error while reading projects file: {e}")


def titleVal():
    title = input("enter project title ")
    if all(not i.isdigit() for i in title) and not title == "":
        project_info.insert(len(project_info), title)
    else:
        print("you entered wrong title format")
        titleVal()


def detailsVal():
    details = input("enter project details ")
    if not details == "":
        project_info.insert(len(project_info), details)
    else:
        print("you entered wrong details format")
        detailsVal()


def targetVal():
    target = input("enter project total target ")
    if all(not i.isalpha() for i in target):
        project_info.insert(len(project_info), target)
    else:
        print("you entered wrong target format")
        targetVal()


def startDateVal():
    start_date = input("enter project start date with following format dd-mm-yyyy ")
    try:
        res = bool(datetime.strptime(start_date, date_format))
    except ValueError:
        res = False
    if res:
        project_info.insert(len(project_info), start_date)
    else:
        print("you entered wrong start date format")
        startDateVal()


def endDateVal():
    end_date = input("enter project end date with following format dd-mm-yyyy ")
    try:
        res = bool(datetime.strptime(end_date, date_format))
    except ValueError:
        res = False
    if res:
        project_info.insert(len(project_info), end_date)
    else:
        print("you entered wrong end date format")
        endDateVal()
