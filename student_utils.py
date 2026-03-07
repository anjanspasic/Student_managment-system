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
            grades_formatted += "\t"+str(grade)
        student_formatted += f" Grades: {grades_formatted}"
        
        if student["active"]==False:
            student_formatted+=' -Dropped out'

        print(student_formatted)


# students = [], property = string, value = string
def find_student_property(students, property, value):

    if property not in ["name","age", "id","active"]:
        print("The property passed was not exisiting")
        return
    
    if property == "id":
        value = int(value)

    if property == "active":
        value = bool(value)
    
    result = []

    for student in students:
        if student[property] == value:
            result.append(student)

    return result

#students-list,id_students-string
def delete_student(students,id_students):
    student_l=find_student_property(students,'id',id_students)
    student=student_l[0]
    if student not in students:
        print('Student doesnt exist')
        return False
    student['active']=False
    return True

def add_grade(students,grade,id_students):
    student_l=find_student_property(students,'id',id_students)
    student=student_l[0]
    if student not in students:
        print('Student doesnt exist')
        return False
    grade=int(grade)
    student['grades'].append(grade)
    return True

def average_grade(student):
    sum=0
    for grade in student['grades']:
        sum+=grade
    return sum/len(student['grades'])
    

def best_3_students(student)





    

    
    

        

