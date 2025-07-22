weight = int(input('Ingrese el peso del paquete (kg): '))
distance = int(input('Ingrese la distancia (km): '))
urgency = input('¿Es urgente? (1. Sí | Otro carácter. No): ')
print()
print('Tamaño del paquete:\n 1. Pequeño\n 2. Mediano\n 3. Grande')
size = int(input('Ingrese el tamaño del paquete: '))

price = 30
print(f'Precio base: Q{price}')

if urgency == '1':
    price += 50
    print('+Q50 por urgencia.')
if size == 3:
    price += 30
    print('+Q30 por tamaño grande.')
if urgency != '1' and weight < 5:
    price -= 20
    print('-Q20 por descuento por envío liviano y no urgente.')

print(f'Total: Q{price}')