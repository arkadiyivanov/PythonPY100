def get_unique_words(str_words: str):
    word_list_without_empty_string = []  # TODO найти список слов в строке исключив пустые строки

    for word in str_words.split(" "):
        if word:
            word_list_without_empty_string.append(word)
    return set(word_list_without_empty_string) # TODO вывести множество уникальных слов


if __name__ == "__main__":
    print(get_unique_words("Здесь много разных слов. Возможно и много повторений."))

