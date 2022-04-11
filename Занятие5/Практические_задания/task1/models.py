
from conf import EMPTY_SYMBOL, SIZE_FIELD
def init_field(size: int = SIZE_FIELD) -> list[list]:
    """

    :param size:
    :return:
    """
    return [
            [EMPTY_SYMBOL for _ in range(size)] for _ in range(size)]
# print(init_field()) #тест поля


def is_empty_cell(field: list[list], row_index: int, col_index: int) -> bool:
    return field[row_index][col_index] == EMPTY_SYMBOL

def has_empty_cell(field: list[list]) -> bool:
    for row in field:
        for cell in row:
            if cell == EMPTY_SYMBOL:
                return True
    return False



def is_win(field: list[list])-> bool:
    win_combinations = [[(0, 0), (0, 1), (0, 2)],
                        [(1, 0), (1, 1), (1, 2)],
                        [(2, 0), (2, 1), (2, 2)],
                        [(0, 0), (1, 0), (2, 0)],
                        [(0, 1), (1, 1), (2, 1)],
                        [(0, 2), (1, 2), (2, 2)],
                        [(0, 0), (1, 1), (2, 2)],
                        [(0, 2), (1, 1), (2, 0)]]
    for win_comb in win_combinations:
        cell_1_coord, cell_2_coord, cell_3_coord = win_comb
        cell_1 = get_cell(field, cell_1_coord[0], cell_1_coord[1])
        cell_2 = get_cell(field, cell_2_coord[0], cell_2_coord[1])
        cell_3 = get_cell(field, cell_3_coord[0], cell_3_coord[1])
        if cell_1 == cell_2 == cell_3 != EMPTY_SYMBOL:
            return True
    return False




def get_cell(field: list[list], row_index: int, col_index: int, player_symbol):
    return field[row_index][col_index] == player_symbol


def set_cell(field: list[list], row_index: int, col_index: int) -> None:
    ...
def test_empty_field():
    empty_field = init_field()
    assert is_win(empty_field) == False


if __name__ == '__main__':
    test_field = init_field()
