def add_student(students):
    name=input('Enter the students name: ')
    age=input('Enter the students age: ')
    id=len(students)+1
    student={'name':name,
             'age':age,
             'grades':[],
             'id':id,
             'active':True}
    students.append(student)

def show_students (students):
    for student in students:
        student_formatted = f"Id: {student['id']}, Name: {student['name']}, Age: {student['age']}"
        #Formatting grades
        grades_formatted = ''
        for grade in student["grades"]:
            grades_formatted += "\t"+grade
        student_formatted += f" Grades: {grades_formatted}"
        
        if student["active"]==False:
            student_formatted+=' -Dropped out'

        print(student_formatted)

def find_student_name(students,student_name):
    same_name=[]
    for student in students:
        if(student['name'] == student_name):
            same_name.append(student)
    return same_name


        

