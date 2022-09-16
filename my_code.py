# Exercise1
x = int(input('Введите длину стороны квадрата: '))
print(f'Периметр: {x*4}')
print(f'Площадь: {x**2}')

a = int(input('Введите длину прямоугольника: '))
b = int(input('Введите ширину прямоугольника: '))
print(f'Периметр: {(a+b)*2}')
print(f'Площадь: {a*b}')

# Exercise3
separator = input()
print(separator*(x*4+a*b))

# Exercise2
month_salary = int(input('Введите заработную плату в месяц: '))
mortgage_percent = int(input('Введите, какой процент(%) уходит на ипотеку: '))
life_percent = int(input('Введите, какой процент(%) уходит на жизнь: '))
year_mortgage_costs = month_salary/100*mortgage_percent*12
year_savings = month_salary/100*(100-mortgage_percent-life_percent)*12
print(f'На ипотеку было потрачено: {int(year_mortgage_costs)} рублей')
print(f'Было накоплено: {int(year_savings)} рублей')
