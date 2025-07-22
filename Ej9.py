days = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']

age = int(input('Ingrese su edad: '))

print('Días:')
j = 1
for i in days:
    print(f'{j}. {i.capitalize()}')
    j+=1
day = int(input('Ingrese un día: '))
day = days[(day-1)]

is_student = int(input('¿Es estudiante? (1. Sí | 2. No): '))

price = 50

if is_student == 1:
    price = 35
if day == 'miércoles':
    price /= 2

if age < 13:
    print('Denegado. Edad por debajo del requerido para ver la película.')
else:
    print(f'Q{price}')
