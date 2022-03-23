A = int(input("Введите число A"))  # TODO
B = int(input("Введите число B"))
C = int(input("Введите число C"))
res = A < 45 and B > 45 and C > 45
res_2 = A > 45 and B < 45 and C > 45
res_3 = A > 45 and B > 45 and C < 45
if res or res_2 or res_3:
    print("Одно из чисел меньше 45 !")
else:
    print("Все числа больше 45")