if __name__ == "__main__":
    list_ = [-1, 5, 48, 63, 32, 26, 78, 12, 32, 10]
    max_value_index = 0
    max_value = list_[max_value_index]
    for i in range(len(list_)):
        current_value = list_[i]
        if current_value >= max_value:
            max_value = current_value
            max_value_index = i
    print(list_)
    list_[max_value_index] = list_[0]
    list_[0] = max_value
    print(list_)






