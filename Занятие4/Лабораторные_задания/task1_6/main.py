if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]

    list_great_first = [num for num in list_ if num > list_[0]]
    print(len(list_great_first))# TODO отфильтровать элементы больше первого
