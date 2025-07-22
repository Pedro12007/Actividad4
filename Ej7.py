students = []

for i in range(5):
    student_data = {}
    name = input('Ingrese el nombre del estudiante: ')
    student_data['name'] = name

    grades = []
    for j in range(3):
        grade = int(input(f'Ingrese la nota del curso #{j+1} (0-100): '))
        grades.append(grade)

    student_data['grades'] = grades
    students.append(student_data)
    print()

