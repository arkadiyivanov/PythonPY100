if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    even_list = [num for num in list_ if num % 2 == 0]
    odd_list = [num for num in list_ if num % 2 == 1]# TODO получить два списка четных и нечетных чисел

    lenght_len_even = len(even_list)
    lenght_len_odd = len(odd_list)
    print(even_list)
    print(odd_list)# TODO найти длины этих списков

    print(lenght_len_even)
    print(lenght_len_odd)
    if lenght_len_even > lenght_len_odd:
        print("Чётных чисел больше")
    elif lenght_len_odd > lenght_len_even:
        print("Нечётных чисел больше")
    else:
        print("Эти списки равны")
    # TODO распечатать каких чисел больше. Учтите, что длины могу быть равны
