incomes = int(input('Ingrese la cantidad de sus ingresos anuales: '))
dependents = int(input('Ingrese la cantidad de dependientes que tiene: '))

taxes = 0
reduction = -1000 * dependents

if incomes < 40000 and dependents > 2:
    taxes = 0
elif incomes <= 30000:
    taxes = incomes * 0.05 + reduction
elif incomes >= 30001 and incomes <= 60000:
    taxes = incomes * 0.1 + reduction
elif incomes >= 60001 and incomes <= 100000:
    taxes = incomes * 0.15 + reduction
elif incomes > 100000:
    taxes = incomes * 0.2 + reduction


print(f'Debe pagar Q{taxes} en impuestos.')