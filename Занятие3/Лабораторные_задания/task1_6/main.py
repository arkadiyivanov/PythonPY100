def sum_many(salary, spend, months = 10, rising_prices = 0.03):
    need_many = 0
    for i in range(months):
        need_many = need_many + spend - salary
        spend *= 1 + rising_prices

    return need_many# TODO написать функцию для поиска необходимой суммы денег


if __name__ == "__main__":
    print(sum_many(5000, 6000))# TODO вызвать функцию и проверить работоспособность
