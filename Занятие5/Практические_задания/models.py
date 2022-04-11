EMPTY_SYMBOL = "-"
SIZE_FIELD = 3

def init_field(size: int = SIZE_FIELD) -> list[list]:
    return [
            [EMPTY_SYMBOL for _ in range(size)] for _ in range(size)]
print(init_field()) #тест поля


def is_empty_cell(field: list[list], row_index: int, col_index: int) -> bool:
    return field[row_index][col_index] == EMPTY_SYMBOL

def has_empty_cell(field: list[list]) -> bool:
    for row in field:
        for cell in row:
            if cell == EMPTY_SYMBOL:
                return True
    return False



def is_win(field: list[list])-> bool:
    ...


def get_cell(field: list[list], row_index: int, col_index: int, player_symbol):
    return field[row_index][col_index] == player_symbol


def set_cell(field: list[list], row_index: int, col_index: int)-> None:
    ...
