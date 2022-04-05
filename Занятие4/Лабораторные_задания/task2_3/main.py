def task(num: int ) -> bool:  # TODO добавить аннотацию типов
    list_num = [int(num) for num in str(abs(num))]
    return True if 10 <= sum(list_num) <= 99 else False  # TODO найти сумму цифр числа и понять двузначная ли она


if __name__ == "__main__":
    print(task(12))
    print(task(555))
    print(task(-12))
    print(task(-149))
