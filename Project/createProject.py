from datetime import datetime

project_info = []
date_format = "%d-%m-%Y"


def createProject(userid: int):
    titleVal()
    detailsVal()
    targetVal()
    startDateVal()
    endDateVal()
    addProject(userid)
    print(project_info)


def addProject(userid):
    try:
        projects_write = open("projects.txt", "a")
        projects_read = open("projects.txt", "r")
        max_id = len(projects_read.readlines())
        projects_write.write(
            str(userid) + "|" + str(int(max_id)) + "|" + str(project_info[0]) + "|" + project_info[1] + "|" + project_info[2] + "|"
            + project_info[3] + "|" + project_info[4] + "\n")
    except Exception as e:
        print(f"error while write project file: {e}")


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
