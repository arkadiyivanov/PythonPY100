def is_palindrome(str_: str):
    str_clear = ''.join(str_.lower().split())

    if str_clear == str_clear[::-1]:
        print("Строка палиндром")
    else:
        print("Строка не палиндром")


if __name__ == "__main__":
    is_palindrome("Кит на море не романтик")
    is_palindrome("Прочая строка")
