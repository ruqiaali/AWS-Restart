names_list = []
names_count = 0
while True:
    student_name = input("please enter a name:")
    if student_name == "stop":
        break
    names_list.append(student_name)
    names_count += 1

    print("the students names are {}" .format(names_list))
    print("there are {} studnets".format(names_count))
    