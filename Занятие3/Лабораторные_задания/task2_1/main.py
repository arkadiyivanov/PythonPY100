def task(str1: str, str2: str, k: int):
    if str1[:k] == str2[:k]:
        print("Да")  # TODO проверка совпадения строк
    else:
        print('Нет')

if __name__ == "__main__":
    task("abc", "abcde", 3)
    task("abcba", "abcde", 5)
