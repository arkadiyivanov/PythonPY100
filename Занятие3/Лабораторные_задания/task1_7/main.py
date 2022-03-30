def live_months(many_capital, salary, spend):
    rising_prices = 0.05
    months = 0
    while many_capital >= spend:
        many_capital -= spend
        months = months + 1
        spend *= 1+ rising_prices
        many_capital += salary
    return months
        # TODO написать функцию для поиска количества месяцев


if __name__ == "__main__":
    print(live_months(150000, 5000, 6000))  # TODO вызвать функцию и проверить работоспособность
