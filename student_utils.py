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



