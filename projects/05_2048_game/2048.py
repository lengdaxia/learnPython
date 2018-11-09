# -*- coding : utf-8 -*-

import curses
from random import randrange,choice
from collections import defaultdict

# 用户行为
actions = ['Up','Left','Down','Right','Restart','Exit']
letter_codes = [ord(ch) for ch in u"WASDRQwasdrq"]
actions_dict = dict(zip(letter_codes,actions*2))


# 获取用户输入
def get_user_action(keyword):
    char = "N"
    while char not in actions_dict:
        char = keyword.getch()
    return actions_dict[char]

# 转置
def transpose(field):
    return [list(row) for row in zip(*field)]

# 矩阵逆转
def invert(field):
    return [row[::-1] for row in field]




# 棋盘
class GameField(object):

    def __init__(self,height=4,width=4,win=2048):
        self.height = height
        self.width = width 
        self.win_value = win  #过关分数
        self.score = 0     #当前分株
        self.highscore = 0  #最高分
        self.reset()  #棋盘重置

# 画棋盘
    def draw(self,screen):
        help_string1 = '(W)Up (S)Down (A)Left (D)Right'
        help_string2 = '    (R)Restart  (Q)Quit'
        game_over = '            Game Over'
        win_string = '              You Win !'

        def cast(string):
            screen.addstr(string + '\n')

        def draw_hor_seperator():
            line = '+' + ('+------' * self.width + '+')[1:]
            seperator = defaultdict(lambda:line)
            if not hasattr(draw_hor_seperator,"counter"):
                draw_hor_seperator.counter = 0
            cast(seperator[draw_hor_seperator.counter])
            draw_hor_seperator.counter += 1

        def draw_row(row):
            cast(''.join('|{: ^5} '.format(num) if num > 0 else '|      ' for num in row) + '|')

        screen.clear()

        cast('SCORE:' + str(self.score))
        if 0 != self.highscore:
            cast('HIGHSCORE:' + str(self.highscore))

        for row in self.field:
            draw_hor_seperator()
            draw_row(row)

        draw_hor_seperator()

        if self.is_win():
            cast(win_string)
        else:
            if self.is_gameover():
                cast(game_over)
            else:
                cast(help_string1)
        cast(help_string2)

    # 棋盘重置
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.field = [[0 for i in range(self.width)] for j in range(self.height)]
        self.spawn()
        self.spawn()

    # 在棋盘的非零区域 随机生成2或者4
    def spawn(self):
        new_element = 4 if randrange(100) > 89 else 2
        (i,j) = choice([ (i,j) for i in range(self.width) for j in range(self.height) if self.field[i][j] == 0])
        self.field[i][j] = new_element

 


    # 对矩阵进行转置和逆转，可以从左移row得到其他方向的移动操作
    def move(self,direction):

        # 向左合并
        def move_row_left(row):
            # 把零散非零单元挤到一块
            def tighten(row):
                new_row = [i for i in row if i != 0]
                new_row += [0 for i in range(len(row) - len(new_row))]
                return new_row

            # 对临近元素进行合并
            def merge(row):
                pair = False
                new_row = []
                for i in range(len(row)):
                    if pair:
                        new_row.append(2*row[i])
                        self.score += 2 * row[i]
                        pair = False
                    else:
                        if i + 1 < len(row) and row[i] == row[i + 1]:
                            pair = True
                            new_row.append(0)
                        else:
                            new_row.append(row[i])
                assert len(new_row) == len(row)
                return new_row
            # 先挤到一块，合并，再挤到一块
            return tighten(merge(tighten(row)))

        moves = {}
        moves['Left'] = lambda field:[move_row_left(row) for row in field]
        moves['Right'] = lambda field:invert(moves['Left'](invert(field)))
        moves['Up'] = lambda field:transpose(moves['Left'](transpose(field)))
        moves['Down'] = lambda field:transpose(moves['Right'](transpose(field)))

        if direction in moves:
            if self.move_is_possible(direction):
                self.field = moves[direction](self.field)
                self.spawn()
                return True
            else:
                return False

    def is_win(self):
        return any(any(i >= self.win_value for i in row) for row in self.field)

    def is_gameover(self):
        return not any(self.move_is_possible(move) for move in actions)

# 是否能走
    def move_is_possible(self,direction):
        def row_is_left_movable(row):
            def change(i):
                if row[i] == 0 and row[i + 1] != 0:
                    return True
                if row[i] != 0 and row[i+1] == row[i]:
                    return True
                return False
            return any(change(i) for i in range(len(row) - 1))

        checks = {}
        checks['Left'] = lambda field:any(row_is_left_movable(row) for row in field)
        checks['Right'] = lambda field:checks['Left'](invert(field))
        checks['Up'] = lambda field:checks['Left'](transpose(field))
        checks['Down'] = lambda field:checks['Right'](transpose(field))

        if direction in checks:
            return checks[direction](self.field)
        else:
            return False


# 状态机，state machine
# 这里是有限状态机 FSM finite state machine

def main(stdscr):

    def init():
        # 重置棋盘
        game_field.reset()
        return 'Game'

    def not_game(state):
        # 画出出事界面
        game_field.draw(stdscr)
        # 获取用户输入
        action = get_user_action(stdscr)

        # 默认是当前状态，没有行为就一直在当前页面循环
        response = defaultdict(lambda:state)
        # 对应不同的行为转换到不同的状态
        response['Restart'],response['Exit'] = 'Init','Exit'

        return response[action]

    def game():

        game_field.draw(stdscr)
        action = get_user_action(stdscr)

        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'

        if game_field.move(action):
            if game_field.is_win():
                return 'Win'
            if game_field.is_gameover():
                return 'GameOver'
        return 'Game'

    state_actions = {
            'Init':init,
            'Win':lambda:not_game('Win'),
            'GameOver':lambda:not_game('GameOver'),
            'Game':game
    }

    curses.use_default_colors()

    game_field = GameField(width=10,height=10 win=2048)

    state = 'Init'

    while state != 'Exit':
        state = state_actions[state]()

curses.wrapper(main)

















