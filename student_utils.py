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
    
def sortStudentsAverageGrade(students, best=True):
    array = []
    for student in students:
        studentIdAverageGrade = {
            "student": student,
            "averageGrade": average_grade(student)
        }
        array.append(studentIdAverageGrade)

    sortedStudents = sorted(array, key=lambda x: x["averageGrade"], reverse=best)

    students = []
    for studentAverageGrade in sortedStudents:
        students.append(studentAverageGrade["student"])

    return students

def pickFirstStudents(students, n):
    pickedStudents = []
    for i in range(n):
        pickedStudents.append(students[i])

    return pickedStudents

def biggerGrade(students):
    bigger_grade_list=[]
    bigger_grade=int(input('Which grade do you want to sort by?'))
    for student in students:
        average=average_grade(student)
        if average>bigger_grade:
            bigger_grade_list.append(student)
    return bigger_grade_list  

