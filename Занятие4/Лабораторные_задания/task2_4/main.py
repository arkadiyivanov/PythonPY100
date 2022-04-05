def digit_sum(num: int) -> bool:
    if len(str(num)) != 4:
        raise ValueError("Число не четырёх значное")  # TODO не забыть проерить, что число дожно быть четырехзначное

    list_num = [int(num) for num in str(num)]
    return True if sum(list_num) % 7 == 0 else False  # TODO проверить кратность суммы цифр


if __name__ == "__main__":
    print(digit_sum(1234))
    print(digit_sum(7777))
