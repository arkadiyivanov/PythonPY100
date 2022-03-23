# Напишите ваше решение
tax = 13
profit = int(input('Введите вашу зарплату'))
size_tax = ((profit/100) * 13)
print('Подоходный налог =', size_tax)
print("Сумма к выдачи",profit-size_tax)