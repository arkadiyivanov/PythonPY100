def task(n: int, m: int) -> list:  # TODO записать функцию с аннотацией типов
    return [num ** 2 for num in range(n, m+1)]  # TODO с помощью list comprehension найти квадраты целых чисел


if __name__ == "__main__":
    number_n = 5
    number_m = 20

    print(task(number_n, number_m))
