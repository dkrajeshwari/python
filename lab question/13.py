def showInfo(student_dict):
    for key,value in student_dict.items():
        print(f"{key}:{value}")

student_dict={"ncet-ec01":"rajesh","ncet-ec02":"mahesh"}
showInfo(student_dict)        