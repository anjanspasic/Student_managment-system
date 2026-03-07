import data
import student_utils

functions='1️⃣ -Add student\n2️⃣ -Show all students\n3️⃣ -Find student by name\n4️⃣ -Delete student\n5️⃣ -Show 3 best students by grade\n6️⃣ -Show 3 worst students by grade\n7️⃣ -Show all student that have bigger grade than\n8️⃣-Add grade'

while True:
    actions=input(functions)
    #sredi formatiranje
    if actions=='1':
        student_utils.add_student(data.students)

    if actions=='2':
        student_utils.show_students(data.students)

    if actions=='3':
        student_name=input('What is the name of the student: ')
        student=student_utils.find_student_property(data.students,'name',student_name)
        student_utils.show_students(student)

    if actions=='4':
        id_students=input('What is id of the student: ')
        succes=student_utils.delete_student(data.students,id_students)
        if succes==True:
            print('You have succesfuly deleted the student')
        else:
            print('Student wasnt deleted')
    if actions=='5':
        print(data.students)
    if actions=='6':
        pass
    if actions=='7':
        pass
    if actions=='8':
        student_id=input('What is id of that student: ')
        grade=int(input('What grade do you wnat to add: '))
        succes=student_utils.add_grade(data.students,grade,student_id)
        if succes==True:
            print('You have succesfuly added the grade')
        else:
            print('Grade wasnt added.')





