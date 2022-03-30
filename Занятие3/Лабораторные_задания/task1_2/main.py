def factorial(n):
    res = 1
    for num in range(1, n):
        res = res * num

    return res
        # TODO запишите здесь функцию factorial


if __name__ == "__main__":
    print(factorial(5))# TODO распечатать результат выполнения функции factorial от числа 5
