projects_ids = []
all_projects = []
project_info = []


def removeProject( project_id):
    try:
        projects_read = open("projects.txt", "r")
        i = 0
        for project in projects_read:
            i += 1
            info = project.split('|')
            if info[1] == projects_ids[project_id-1]:
                j = i-1
                all_projects.pop(j)
                print("deleted successfully")
                projects_write = open("projects.txt", "w")
                projects_write.writelines(all_projects)

    except Exception as e:
        print(f"error while write project file: {e}")


def delete(userid):
    value = input("select project to delete ")
    if not int(value) > len(projects_ids):
        project_info.clear()
        removeProject(int(value))
    else:
        print("you entered wrong choice")
        delete(userid)


def deleteProject(userid):
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
            delete(userid)
        else:
            print("you dont created projects yet")
    except Exception as e:
        print(f"error while reading projects file: {e}")
