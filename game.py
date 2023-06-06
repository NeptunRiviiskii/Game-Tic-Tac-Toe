import numpy as np


class Game:
    """Класс представляющий игру"""

    def __init__(self, text=None):
        """Инициализация объектов игры"""

        self.text = text
        self.messages = text[0]
        self.player1 = Player(self.messages, 'Player-1', 'X')
        self.player2 = Player(self.messages, 'Player-2', 'O')
        self.sheet = GameTable()
        self.num_of_game = 0
        self.game_mode = None
        self.table = ['11', '12', '13',
                      '21', '22', '23',
                      '31', '32', '33']

    def get_game_mode(self):
        """Получение игрового режима"""

        print(self.messages['menu']['ask3'])
        game_mode = input(f"{self.messages['system_mes']['choice']}")
        if game_mode not in ['1', '2']:
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            print(self.messages['system_mes']['error'])
            return self.get_game_mode()
        return game_mode

    def set_game_mode(self):
        """Выбор режима игры """

        self.game_mode = self.get_game_mode()
        if self.game_mode == '1':
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            self.player1.set_player_name()
            self.mode_pve()
        if self.game_mode == '2':
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            self.player1.set_player_name()
            print('')
            self.player2.set_player_name()
            self.mode_pvp()

    def check_status(self, player_fig):
        """Проверка таблицы на выигрыш или проигрыш"""

        for i in range(3):
            if self.sheet.table[0][i] == self.sheet.table[1][i] == self.sheet.table[2][i] == player_fig:
                return 'w'
            elif self.sheet.table[i][0] == self.sheet.table[i][1] == self.sheet.table[i][2] == player_fig:
                return 'w'
            elif self.sheet.table[0][0] == self.sheet.table[1][1] == \
                    self.sheet.table[2][2] == player_fig:
                return 'w'
            elif self.sheet.table[0][2] == self.sheet.table[2][2] == \
                    self.sheet.table[2][0] == player_fig:
                return 'w'

    def get_statistic(self):
        """Создание и выдача статистики по игре."""

        p1_stat = [self.player1.num_of_wins, self.player1.num_of_lose,
                   self.player1.num_of_draw]
        p2_stat = [self.player2.num_of_wins, self.player2.num_of_lose,
                   self.player2.num_of_draw]
        return p1_stat, p2_stat

    def win_mode(self, winner, loser):
        """Действия после победы одного из игроков"""

        winner.get_game_results('w')
        loser.get_game_results('l')
        self.num_of_game += 1
        self.sheet.describe_table_on_console()
        print(f"{winner.player_name} {self.messages['system_mes']['win']}")

    def reset_mode(self):
        """Обнуление данных в рамках игры"""

        self.table = ['11', '12', '13',
                      '21', '22', '23',
                      '31', '32', '33']
        self.sheet.__init__()

    def draw_mode(self, player1, player2):
        """Действия после ничьей"""

        player1.get_game_results('d')
        player2.get_game_results('d')
        self.num_of_game += 1
        print(self.messages['system_mes']['draw'].center(15))

    def mode_pvp(self):
        """Режим игры ПвП"""

        self.sheet.describe_table_on_console()
        while True:
            # Ход 1-ого игрока
            p1 = self.player1.set_position(self.table)
            self.table.remove(f'{p1[0]}{p1[1]}')
            self.sheet.set_fig_on_table(p1, self.player1.play_fig)
            self.sheet.describe_table_on_console()
            p1_status = self.check_status(self.player1.play_fig)
            if p1_status:
                self.win_mode(self.player1, self.player2)
                break
            if not self.table:
                self.draw_mode(self.player1, self.player2)
                break
            # Ход 2-ого игрока
            p2 = self.player2.set_position(self.table)
            self.table.remove(f'{p2[0]}{p2[1]}')
            self.sheet.set_fig_on_table(p2, self.player2.play_fig)
            self.sheet.describe_table_on_console()
            p2_status = self.check_status(self.player2.play_fig)
            if p2_status:
                self.win_mode(self.player2, self.player1)
                break
            if not self.table:
                self.draw_mode(self.player1, self.player2)
                break

    def mode_pve(self):
        """Режим игры ПвЕ"""

        self.sheet.describe_table_on_console()
        while True:
            # Ход 1-ого игрока
            p1 = self.player1.set_position(self.table)
            self.table.remove(f'{p1[0]}{p1[1]}')
            self.sheet.set_fig_on_table(p1, self.player1.play_fig)
            p1_status = self.check_status(self.player1.play_fig)
            if p1_status:
                self.win_mode(self.player1, self.player2)
                break
            if not self.table:
                self.draw_mode(self.player1, self.player2)
                break
            # Ход 2-ого игрока
            p_2 = str(np.random.choice(self.table))
            p2 = [int(p_2[0]), int(p_2[1])]
            self.table.remove(f'{p2[0]}{p2[1]}')
            self.sheet.set_fig_on_table(p2, self.player2.play_fig)
            self.sheet.describe_table_on_console()
            p2_status = self.check_status(self.player2.play_fig)
            if p2_status:
                self.win_mode(self.player2, self.player1)
                break
            if not self.table:
                self.draw_mode(self.player1, self.player2)
                break

# ----------------------------------------------------------------------------------------------------------------------


class Player:
    """Представляет обычного игрока"""

    def __init__(self, messages, player_name='', figure_xo=None):
        """Иницивлизация параметров игрока"""

        self.messages = messages
        self.player_name = player_name
        self.play_fig = figure_xo
        self.num_of_wins = 0
        self.num_of_lose = 0
        self.num_of_draw = 0

    def get_game_results(self, status: str):
        """Изменение игрового статуса"""

        mes_status = ['w', 'l', 'd']
        if status == mes_status[0]:
            self.num_of_wins += 1
        elif status == mes_status[1]:
            self.num_of_lose += 1
        elif status == mes_status[2]:
            self.num_of_draw += 1

    def set_player_name(self):
        """Изменение имени игрока"""

        print('')
        player_name = input(self.messages['system_mes']['name'])
        if player_name == '':
            pass
        elif len(player_name) > 11:
            print(self.messages['system_mes']['name_info'])
            self.set_player_name()
        else:
            self.player_name = player_name.title()

    def set_position(self, table):
        """Полчуение координаты"""

        position = input(f' {self.player_name}, {self.messages["system_mes"]["go"]}')
        if position not in table:
            print('')
            print(self.messages['system_mes']['error'])
            pos = self.set_position(table)
            return pos
        return [int(position[0]), int(position[1])]


# ----------------------------------------------------------------------------------------------------------------------


class GameTable:
    """Представление игрового поля"""

    def __init__(self):
        """Инициализация игрового поля"""

        self.table = np.full((3, 3), '-')

    def set_fig_on_table(self, ij, fig):
        """Установка хода игрока"""

        self.table[ij[0] - 1][ij[1] - 1] = fig

    def describe_table_on_console(self):
        """Отображение игрового поля на консоле"""

        print(f'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t   ▁▁▁▁▁▁▁\n'
              f'\t1  ┃{self.table[0][0]}┃{self.table[0][1]}┃{self.table[0][2]}┃\n'
              f'\t2  ┃{self.table[1][0]}┃{self.table[1][1]}┃{self.table[1][2]}┃\n'
              f'\t3  ┃{self.table[2][0]}┃{self.table[2][1]}┃{self.table[2][2]}┃\n'
              f'\t   ▔▔▔▔▔▔▔\n\t    1 2 3')
