if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    even_list = [num for num in list_ if num % 2 == 0]
    odd_list = [num for num in list_ if num % 2 == 1]
    print(even_list)
    print(odd_list)
    # TODO получить два списка четных и нечетных чисел
    #
    length_even_list = len(even_list)  # TODO найти длины этих списков
    length_odd_list = len(odd_list)

    if length_even_list > length_odd_list:
        print("Чётных чисел больше")
    elif length_odd_list > length_even_list:
        print("Нечётных чисел больше")
    else:
        print("Эти списки равны")# TODO распечатать каких чисел больше. Учтите, что длины могу быть равны
