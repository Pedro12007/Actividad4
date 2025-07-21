users = [{'user': 'Juan', 'password': '123abcd'},
         {'user': 'Carlos', 'password': 'abcd123'},
         {'user': 'Pablo', 'password': 'abcd1234'}]

attempts = 3

while attempts > 0:
    user = input('Ingrese su usuario: ')
    password = input('Ingrese su contraseña: ')

    user_num = 0
    for i in users:
        if user == i['user']:
            break
        else:
            user_num += 1

    if user_num == 3:
        attempts -= 1
        print(f'No existe el usuario. Intentos restantes: {attempts}\n')
        continue

    if password != users[user_num]['password']:
        attempts -= 1
        print(f'Contraseña incorrecta. Intentos restantes: {attempts}\n')
        continue
    else:
        print('INICIO DE SESIÓN EXITOSO\n')
        break

if attempts == 0:
    print('ACCESO BLOQUEADO')
else:
    while True:
        print('Opciones: \n1. Ver perfil. \n2. Cambiar contraseña. \n3. Cerrar sesión.')
        option = int(input('Ingrese una opción: '))

        if option == 1:
            print(f'Tu usuario es: {users[user_num]['user']}')