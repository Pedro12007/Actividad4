day_1 = int(input('Ingrese un día: '))
month_1 = int(input('Ingrese un mes: '))
year_1 = int(input('Ingrese un año: '))
day_2 = int(input('Ingrese otro día: '))
month_2 = int(input('Ingrese otro mes: '))
year_2 = int(input('Ingrese otro año: '))


days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def total_days(day, month, year):
    total = year * 365
    for i in range(month - 1):
        total += days_per_month[i]
    total += day
    return total

if year_1 > year_2 or (year_1 == year_2 and month_1 > month_2) or (year_1 == year_2 and month_1 == month_2 and day_1 > day_2):
    print("La primera fecha es mayor.")
    if year_1 == year_2 and month_1 and month_2:
        print('Están en el mismo mes y año.')
elif year_1 == year_2 and month_1 == month_2 and day_1 == day_2:
    print("Ambas fechas son iguales.")
    if year_1 == year_2 and month_1 and month_2:
        print('Están en el mismo mes y año.')
else:
    print("La segunda fecha es mayor.")
    if year_1 == year_2 and month_1 and month_2:
        print('Están en el mismo mes y año.')

total_days_1 = total_days(day_1, month_1, year_1)
total_days_2 = total_days(day_2, month_2, year_2)
print(f'Diferencia: {abs(total_days_1-total_days_2)} días.')