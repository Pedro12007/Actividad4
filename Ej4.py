subtotal = 0

product_amount = int(input('Ingrese la cantidad de productos a comprar: '))
for i in range(product_amount):
    price = float(input('Ingrese el precio del producto:'))
    subtotal += price

ask_tip = int(input('¿Desea dejar propina? (1. Sí | 2. No): '))
if ask_tip == 1:
    tip = int(input('¿Cuánto? (%): '))

frequent_client_card = int(input('¿Posee tarjeta de cliente frecuente? (1. Sí | 2. No): '))

print('Total detallado')
print(f'Subtotal: Q{subtotal}')

taxes = round(subtotal*0.12, 2)
print(f'IVA: Q{taxes}')

if ask_tip == 1:
    tip = round(subtotal*(tip/100), 2)
    print(f'Propina: Q{tip}')
else:
    tip = 0
    print('Propina: Q0.00')

if frequent_client_card == 1:
    discount = round(subtotal*0.10, 2)
else:
    discount = 0
print(f'Descuento: Q{discount}')

total = round(subtotal + taxes + tip - discount, 2)
print(f'Total: Q{total}')