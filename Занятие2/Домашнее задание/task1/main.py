if __name__ == "__main__":
    list_ = [4, 6, 10, -10, 3, 23, -1, 8, 6, 9]

    # предположим, что первый элемент в нашем списке минимальный
    min_value_index = 0
    min_value = list_[min_value_index]

    for i, current_value in enumerate(list_):
        if current_value <= min_value:
            min_value = current_value
            min_value_index = i

    print("Минимальный элемент =", min_value, "находится по индексу", min_value_index)
