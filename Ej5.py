day = int(input('Ingrese un día: '))
month = int(input('Ingrese un mes: '))
year = int(input('Ingrese un año: '))

leap_year = (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))
check_30_days = (month<=6 and (month%2==0) and (month!=2)) or (month>=9 and (month%2!=0))
check_31_days = (month<=7 and (month%2!=0)) or (month>=8 and (month%2==0))

check_month = ((month == 2 and ((leap_year and day <= 29) or (not leap_year and day <= 28))) or
                    (check_30_days and day <= 30) or
                    (check_31_days and day <= 31))

if check_month and day > 0 and 12 >= month > 0 and 9999 >= year >= 1000:
    pass
else:
    print('Fecha inválida.')
