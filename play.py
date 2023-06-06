from text import messages
from game import Game


def play():
    """Запуск игрового процесса"""

    game = Game(messages)
    print('')
    print('*****'.center(50, '-'))
    print(game.messages['menu']['greetings'].center(50))
    print('*****'.center(50, '-'))
    print('')
    _ = input(game.messages['menu']['enter'].center(50))
    space()
    while True:
        ask_1(game)
        ask_2(game)


def space():
    """Имитация смены кадра/окна"""
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')


def ask_1(game):
    """Диалоговая функция, меню-1"""

    print(game.messages['menu']['ask1'])
    ask = input(game.messages['system_mes']['choice'])
    if ask not in ['1', '2', '3', '4', '5']:
        space()
        print(game.messages['system_mes']['error'])
        ask_1(game)
    if ask == '1':
        space()
        game.set_game_mode()
    if ask == '2':
        space()
        instruction(game)
    if ask == '3':
        space()
        about(game)
    if ask == '4':
        space()
        change_language(game)
    if ask == '5':
        space()
        print('*****'.center(50, '-'))
        print(game.messages['system_mes']['exit'].center(50))
        print('*****'.center(50, '-'))
        return exit()


def ask_2(game):
    """Диалоговая функция, меню-2"""

    print(game.messages['menu']['ask2'])
    ask = input(game.messages['system_mes']['choice'])
    if ask not in ['1', '2', '3']:
        space()
        print(game.messages['system_mes']['error'])
        ask_2(game)
    if ask == '1':
        game.reset_mode()
        if game.game_mode == '1':
            game.mode_pve()
        if game.game_mode == '2':
            game.mode_pvp()
        ask_2(game)
    if ask == '2':
        space()
        information(game)
        ask_2(game)
    if ask == '3':
        space()
        game.num_of_game = 0
        game.player1.player_name = 'Player-1'
        game.player2.player_name = 'Player-2'
        game.reset_mode()


def information(game):
    """Вывод статистики по игре"""

    print(game.messages['menu']['statistic'][0])
    p1_stat, p2_stat = game.get_statistic()

    print(f" {game.player1.player_name} ".ljust(15, '-'), f"> "
          f"| {game.messages['menu']['statistic'][1]} {p1_stat[0]} | "
          f"{game.messages['menu']['statistic'][2]} {p1_stat[1]} |", sep='-')

    print(f" {game.player2.player_name} ".ljust(15, '-'), f"> "
          f"| {game.messages['menu']['statistic'][1]} {p2_stat[0]} | "
          f"{game.messages['menu']['statistic'][2]} {p2_stat[1]} |", sep='-')
    print(f" {game.messages['menu']['statistic'][3]} {p1_stat[2]}")

    print(game.messages['menu']['back'])
    ask = input(game.messages['system_mes']['choice'])
    if ask != '1':
        space()
        print(game.messages['system_mes']['error'])
        information(game)
    if ask == '1':
        space()
        pass


def instruction(game):
    """Вывод инструкции игры"""

    print('▁'*46)
    print(game.messages['instruction'])
    print('▔'*46)

    print(game.messages['menu']['back'])
    ask = input(game.messages['system_mes']['choice'])
    if ask != '1':
        space()
        print(game.messages['system_mes']['error'])
        instruction(game)
    if ask == '1':
        space()
        ask_1(game)


def about(game):
    """Вывод информации об игре и её создатели"""

    print('▁'*46)
    print('┃', game.messages['about'][0].center(42), '┃')
    print('┃', game.messages['about'][1].center(42), '┃')
    print('┃', game.messages['about'][2].center(42), '┃')
    print('┃', game.messages['about'][3].center(42), '┃')
    print('▔'*46)
    print('')
    print(game.messages['menu']['back'])
    ask = input(game.messages['system_mes']['choice'])
    if ask != '1':
        space()
        print(game.messages['system_mes']['error'])
        about(game)
    if ask == '1':
        space()
        ask_1(game)


def change_language(game):
    """Изменяет язык игры"""
    print(game.messages['menu']['ask4'])
    ask = input(game.messages['system_mes']['choice'])
    if ask not in ['1', '2', '3']:
        space()
        print(game.messages['system_mes']['error'])
        change_language(game)
    if ask == '1':
        game.messages = game.text[0]
        game.player1.messages = game.text[0]
        game.player2.messages = game.text[0]
        space()
        ask_1(game)
    if ask == '2':
        space()
        game.messages = game.text[1]
        game.player1.messages = game.text[1]
        game.player2.messages = game.text[1]
        ask_1(game)
    if ask == '3':
        space()
        ask_1(game)
