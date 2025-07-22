print('Coordenadas: \n1. Norte \n2. Sur \n3. Este \n4. Oeste')
origin = input('Ingrese la coordenada de origen: ')
destination = input('Ingrese la coordenada del destino: ')

str_coordinates = {
    '1': 'norte',
    '2': 'sur',
    '3': 'este',
    '4': 'oeste'
}
origin = str_coordinates[origin]
destination = str_coordinates[destination]

if origin == destination:
    print(f'Ya estás en {destination}.')
if origin == 'norte' and destination == 'sur':
    print('Recto hacia el sur')
if origin == 'sur' and destination == 'norte':
    print('Recto hacia el norte')
if origin == 'este' and destination == 'oeste':
    print('Recto hacia el oeste')
if origin == 'oeste' and destination == 'este':
    print('Recto hacia el este')

if origin == 'norte' and destination == 'este':
    print('Sureste')
if origin == 'norte' and destination == 'oeste':
    print('Suroeste')
if origin == 'sur' and destination == 'este':
    print('Noreste')
if origin == 'sur' and destination == 'oeste':
    print('Noroeste')
if origin == 'este' and destination == 'norte':
    print('Noroeste')  
if origin == 'este' and destination == 'sur':
    print('Suroeste')
if origin == 'oeste' and destination == 'norte':
    print('Sureste')
if origin == 'oeste' and destination == 'sur':
    print('Noreste')