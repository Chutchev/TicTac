import random


def player_choose():
    player = input("За кого вы будете играть?\n")
    while player.lower() != 'x' and player.lower() != 'o' and player.lower() != 'х' and player.lower() != 'о':
        player = input("За кого вы будете играть?\n")
    if player.lower() == 'x':
        comp = 'o'
    else:
        comp = 'x'
    return player.upper(), comp.upper()


def first_move(player):
    if player.lower() == 'x':
        return 'player'
    else:
        return 'comp'


def player_move(game_field, moves_list, player):
    chosen_cell = int(input("Ваш ход. Введите номер клетки\n"))
    error = False
    for cell in moves_list:
        if cell == chosen_cell:
            game_field[chosen_cell] = f'|_{player}_|'
            moves_list.remove(chosen_cell)
            error = False
            break
        else:
            error = True
    if error == True:
        print('Вы не можете сходить в эту клетку. Она уже занята или ее не существует!')
        print_game_field(game_field)
        player_move(game_field, moves_list, player)


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
    continue_game = True
    for index in range(3):
        if game_field[index] == game_field[index+1] and game_field[index] == game_field[index + 2]:
            continue_game = False
        elif game_field[index] == game_field[index + 3] and game_field[index] == game_field[index + 6]:
            continue_game = False
    if game_field[0] == game_field[4] and game_field[0] == game_field[8]:
        continue_game = False
    elif game_field[2] == game_field[4] and game_field[2] == game_field[6]:
        continue_game = False
    return continue_game


def first_player_move(game_field, moves_list, player, comp):
    while True:
        print_game_field(game_field)
        if len(moves_list) > 0 and check_winner(game_field):
            player_move(game_field, moves_list, player)
        else:
            print_game_field(game_field)
            print('Выиграл компьютер!')
            break
        if len(moves_list) > 0 and check_winner(game_field):
            comp_move(game_field, moves_list, comp)
        else:
            print_game_field(game_field)
            print('Вы выиграли!')
            break


def first_comp_move(game_field, moves_list, player, comp):
    while True:
        if len(moves_list) > 0 and check_winner(game_field):
            comp_move(game_field, moves_list, comp)
            print_game_field(game_field)
        else:
            print_game_field(game_field)
            print('Вы выиграли!')
            break
        if len(moves_list) > 0 and check_winner(game_field):
            player_move(game_field, moves_list, player)
        else:
            print_game_field(game_field)
            print('Выиграл компьютер!')
            break


def main():
    player, comp = player_choose()
    game_field = ['|_0_|', '|_1_|', '|_2_|', '|_3_|', '|_4_|', '|_5_|', '|_6_|', '|_7_|', '|_8_|']
    moves_list = [i for i in range(0, 9)]
    first = first_move(player)
    if first == 'player':
        first_player_move(game_field, moves_list, player, comp)
    else:
        first_comp_move(game_field, moves_list, player, comp)


if __name__ == '__main__':
    main()



