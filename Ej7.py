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


def get_average():
    averages = []
    under_70 = 0
    for i in range(len(students)):
        sum = 0
        for grade in students[i]['grades']:
            sum += grade
        average = round(sum/len(students[i]['grades']), 2)
        averages.append(average)

        if average < 70:
            under_70 += 1

    return averages, under_70

if len(get_average()[0]) == get_average()[1]:
    for i in range(len(students)):
        for j in range(len(students[i]['grades'])):
            if students[i]['grades'][j] <= 95:
                students[i]['grades'][j] += 5

print(f'|{'Nombre':<15}|{'Promedio':<10}|')
print('-'*28)
for i in range(len(students)):
    print(f'|{students[i]['name']:<15}|{get_average()[0][i]:<10}|')
print('-'*28)