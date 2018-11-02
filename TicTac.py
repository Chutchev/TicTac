import random


def player_choose():
    player = input("За кого вы будете играть?\n")
    if player.lower() != 'x' and player.lower() != 'o':
        player_choose()
    if player.lower() == 'x':
        comp = 'o'
    else:
        comp = 'x'
    return player.upper(), comp.upper()


def player_move(game_field, moves_list, player):
    chosen_cell = int(input("Введите номер клетки\n"))
    game_field[chosen_cell] = f'|_{player}_|'
    moves_list.remove(chosen_cell)


def comp_move(game_field, moves_list, comp):
    chosen_cell = random.choice(moves_list)
    game_field[chosen_cell] = f'|_{comp}_|'
    moves_list.remove(chosen_cell)


def print_game_field(game_field):
    print()
    print(f"{game_field[0]}{game_field[1]}{game_field[2]}")
    print(f"{game_field[3]}{game_field[4]}{game_field[5]}")
    print(f"{game_field[6]}{game_field[7]}{game_field[8]}")
    print()


def check_winner(game_field):
    if game_field[0] == game_field[1] and game_field[1] == game_field[2]:
        return False
    elif game_field[0] == game_field[4] and game_field[0] == game_field[8]:
        return False
    elif game_field[0] == game_field[3] and game_field[0] == game_field[6]:
        return False
    elif game_field[3] == game_field[4] and game_field[3] == game_field[5]:
        return  False
    elif game_field[6] == game_field[7] and game_field[6] == game_field[8]:
        return False
    elif game_field[1] == game_field[4] and game_field[1] == game_field[7]:
        return False
    elif game_field[2] == game_field[5] and game_field[2] == game_field[8]:
        return False
    elif game_field[2] == game_field[4] and game_field[2] == game_field[6]:
        return False
    else:
        return True


def main():
    player, comp = player_choose()
    game_field = ['|_0_|', '|_1_|', '|_2_|', '|_3_|', '|_4_|', '|_5_|', '|_6_|', '|_7_|', '|_8_|']
    moves_list = [i for i in range(0, 9)]
    continue_game = True
    while continue_game == True:
        print_game_field(game_field)
        if len(moves_list) > 0 and check_winner(game_field):
            player_move(game_field, moves_list, player)
        else:
            print_game_field(game_field)
            print('Выиграл Компутер')
            continue_game = False
        if len(moves_list) > 0 and check_winner(game_field):
            comp_move(game_field, moves_list, comp)
        else:
            print_game_field(game_field)
            print('Выиграл Игрок')
            continue_game = False


if __name__ == '__main__':
    main()



