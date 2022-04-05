if __name__ == "__main__":
    number = 123456789

    list_digits = [int(digit) for digit in str(number)] # TODO c помощью list comprehension получить список цифр числа
    print(list_digits)

    print(sum(set(list_digits)))  # TODO найти сумму цифр числа

    print(sum([even_num for even_num in list_digits if even_num % 2 == 0]))  # TODO найти сумму всех четных чисел

    print(len(list_digits))  # TODO найти количество цифр

    print(min(list_digits))  # TODO найти минимальную цифру

    print(list_digits[::2])  # TODO все цифры стоящие на нечетных местах

    print(list_digits[0] - list_digits[8])  # TODO найти разность между первой и последней цифрой
