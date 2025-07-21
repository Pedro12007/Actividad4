while True:
    name = input('Ingrese su nombre completo: ')
    if len(name) < 5:
        print('El nombre debe contener como mínimo 5 letras. Intente nuevamente')
    else:
        break

while True:
    dpi = input('Ingrese su DPI: ')

    letters = 0
    for i in dpi:
        if not i.isdigit():
            letters += 1
    if len(dpi) != 13:
        print('El DPI debe tener 13 números.')
    elif letters != 0:
        print('Solo debe contener números.')
    else:
        break

department = input('Ingrese su departamento de origen: ')
birth_year = int(input('Ingrese su año de nacimiento: '))

valid = False
voting_age = 18

if department == 'Alta Verapaz' or department == 'Peten':
    voting_age = 17

if 2025 - birth_year <= voting_age:
    print('Votante no válido.')
else:
    print(f'Bienvenido {name}, su centro de votación está en {department}.')