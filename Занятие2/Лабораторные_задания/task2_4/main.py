if __name__ == "__main__":
    phrase = "Hello,world"
    initial_offset = 5
    for offset, char in enumerate(phrase, start=initial_offset):
        print(" " * offset, char)  # TODO как использовать начальное смещение в команде enumerate?
