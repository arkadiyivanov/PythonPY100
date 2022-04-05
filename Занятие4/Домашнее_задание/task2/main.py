def task(num: int) -> bool:
    list_num = [int(num) for num in str(num)]
    return False if len(set(list_num)) == len(list_num) else True # TODO какая есть отличительная особенность, при повторяющихся числах


if __name__ == "__main__":
    print(task(123))
    print(task(1111111))
