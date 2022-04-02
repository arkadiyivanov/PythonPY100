def input_numbers():
    list_numbers = 0

    while True:
        input_num = int(input("Введите новое число"))
        if input_num < 0:
            break
        if 3 <= input_num <= 13:
            list_numbers.append(input_num)

    return list_numbers # TODO выберите нужный цикл, чтобы получать числа с клавиатуры

    while input_num > 0:
if __name__ == "__main__":
    numbers = input_numbers()
    print(numbers)


