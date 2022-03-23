if __name__ == "__main__":
    list_ = [-1, 5, 48, 63, 32, 26, 78, 12, 32, 10]
    max_value = list_[0]
    max_value_index = 0
    max_value1 = list_[max_value_index]
    for i in range(len(list_)):
        current_value = list_[i]
        max_value = current_value
        max_index = i

    for current_value in list_:
        if current_value > max_value:
            max_value = current_value
        print("Найден максимальный элемент = ", max_value)

    list_[0] = max_index
    max_value1
    print(list_)

