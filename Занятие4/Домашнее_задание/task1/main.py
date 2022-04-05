def task(num: int) -> bool:
    list_num = [int(num) for num in str(num)]
    return True if len(set(list_num)) == 1 else False# TODO какая есть особенность, когда все цифры в числе одинаковые?


if __name__ == "__main__":
    print(task(123))
    print(task(44444))
