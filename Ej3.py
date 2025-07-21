users = [{'user': 'Juan', 'password': '123abcd'},
         {'user': 'Carlos', 'password': 'abcd123'},
         {'user': 'Pablo', 'password': 'abcd1234'}]

attempts = 3

while attempts > 0:
    user = input('Ingrese su usuario: ')
    password = input('Ingrese su contraseña: ')

    counter = 0
    for i in users:
        if user != i['user']:
            counter += 1
    if counter == 3:
        attempts -= 1
        print(f'No existe el usuario. Intentos restantes: {attempts}\n')
        continue

    if password != users[counter]['password']:
        attempts -= 1
        print(f'Contraseña incorrecta. Intentos restantes: {attempts}\n')
        continue

if attempts == 0:
    print('ACCESO BLOQUEADO')
