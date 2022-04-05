def input_numbers():
    numbers_list = []
    while True:
        number = int(input("Введите число: "))
        if 3 <= number <= 13:
            numbers_list.append(number)

        if number < 0:
            numbers_list.append(number)
            break

    return numbers_list


if __name__ == "__main__":
    numbers = input_numbers()
    print(numbers)

