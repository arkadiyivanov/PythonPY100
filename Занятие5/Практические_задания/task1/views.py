#views
"""

"""
from models import init_field, is_win, has_empty_cell, is_empty_cell, set_cell
from conf import EMPTY_SYMBOL, SIZE_FIELD, SECOND_PLAYER, FIRST_PLAYER


def main():
    field = init_field()
    print_field(field)
    current_player, next_player = FIRST_PLAYER, SECOND_PLAYER
    dict_players_step ={ FIRST_PLAYER: player_step, SECOND_PLAYER: enemy_step}
    while True:
        current_player_step_func = dict_players_step[current_player]
        current_player_step_func(field, current_player)
        print_field(field)
        if is_win(field):
            print_win_massage(current_player)
            break
        if not has_empty_cell(field):
            print_draw_massage()
            break

        current_player, next_player = next_player, current_player


def player_step(field, player_symbol: str):
    while True:
        try:
            coord = int(input("Введите номер  ячейки для хода"))
        except ValueError:
            print("Вы ввели неверное число")
            continue
        if not 1 <= coord <= 9:
            print("Введите число от 1 до 9")
            continue
        x = (coord - 1) // SIZE_FIELD
        y = (coord - 1) % SIZE_FIELD
        if not is_empty_cell(field, row_index=x, col_index=y):
            print("Ячейка занята")
            continue
        set_cell(field, row_index=x, col_index=y, player_symbol)


def enemy_step(field, player_symbol: str):
    player_step(field, player_symbol)



def print_field(field: list[list]) -> None:
    start_num = 1
    for i in range(len(field)):
        for j in range(len(field[i])):
            print_symbol = start_num if field[i][j] == EMPTY_SYMBOL else field[i][j]
            start_num +=1
            print(print_symbol, end=" ")
        print()
    print("-"*20)

def print_win_massage(player_symbol: str) -> None:
    print(f"Выйграл игрок{player_symbol}")

def print_draw_massage():
    print(f"Ничья")


if __name__== "__main__":
    main()