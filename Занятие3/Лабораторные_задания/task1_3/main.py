def get_list_number_divisors(number):
    list_dev = []
    for dev in range(1, number+1):
        if number % dev == 0:
            list_dev.append(dev)
    return list_dev

        # TODO найти список делителей числа number


if __name__ == "__main__":
    print(get_list_number_divisors(2 ** 10))
