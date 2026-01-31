import data
import student_utils

functions='1️⃣ -Add student\n2️⃣ -Show all students\n3️⃣ -Find student by name\n4️⃣ -Delete student\n5️⃣ -Show 3 best students by grade\n6️⃣ -Show 3 worst students by grade\n7️⃣ -Show all student that have bigger grade than\n8️⃣-Add grade'

while True:
    actions=input(functions)
    if actions=='1':
        student_utils.add_student(data.students)

    if actions=='2':
        student_utils.show_students(data.students)

    if actions=='3':
        student_name=input('What is the name of the student: ')
        student=student_utils.find_student_name(data.students,student_name)
        student_utils.show_students(student)

    if actions=='4':
        pass
    if actions=='5':
        pass
    if actions=='6':
        pass
    if actions=='7':
        pass




