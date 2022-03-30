PI = 3.14
r = int(input("Введите радиус круга:  "))

def square_circle(r):
    return PI * r ** 2


if __name__ == "__main__":
    square = square_circle(r)
    print(square)
