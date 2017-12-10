#!/usr/bin/env python
import random
import sys

class Game(object):
    def __init__(self, size=8, maxbombs=3):
        self.size = size
        self.maxbombs = maxbombs if maxbombs else 1
        self.board = [['[_]' for i in range(self.size)] for i in range(self.size)]
        self.bombs = []
        self.face = ':|'
        self.place_bombs()


    def place_bombs(self):
        for x in range(self.size):
            bombcount = random.choice([1, self.maxbombs])
            bombs_placed = 0
            for y in range(self.size):
                if bombs_placed < bombcount:
                    place = random.choice([True, False])
                    if place:
                        self.bombs.append((x, y))
                        bombs_placed += 1
                else:
                    break
                 
 
    def draw_board(self):
        print(self.face)
        for row in self.board:
            print(''.join(row))


    def move(self, x, y):
        if (x < 0):
            print('{} (x) < 0'.format(x))
        elif (x >= self.size):
            print('{} (x) > {}'.format(x, self.size))
        elif (y < 0):
            print('{} (y) < 0'.format(y))
        elif (y >= self.size):
            print('{} (y) > {}'.format(y, self.size))
        elif self.board[x][y] == '-_-':
            print('Already went there!')
        else:
            if (x,y) in self.bombs:
                self.board[x][y] = "[*]"
                print('BOOM!!!')
                return 'bad'
            else:
                self.board[x][y] = self.calculate(x, y)
                return 'good'


    def calculate(self, x, y):
        surrounding_ct = 0
        possible_bombs = [
            (x - 1, y - 1),
            (x - 1, y),
            (x - 1, y + 1),
            (x, y - 1),
            (x, y + 1),
            (x + 1, y - 1),
            (x + 1, y),
            (x + 1, y + 1)
        ] 
        try:
            for poss in possible_bombs:
                if poss in self.bombs:
                    surrounding_ct += 1
        except IndexError:
            pass   
        return '[{}]'.format(surrounding_ct)


def main():
    gamesize = raw_input('Choose board size (enter for default (8))').strip()
    if gamesize.isdigit():
        game = Game(int(gamesize), int(gamesize)//2 - 1)
    else:
        game = Game()
    while True:
        won = True
        for row in range(game.size):
            for col in range(game.size):
                if game.board[row][col] == '[_]' and (row, col) not in game.bombs:
                    won = False
        if won:
            game.face = ':)'
            game.draw_board()
            print('Congrats!! You Won!')
            sys.exit()
        game.draw_board()
        move = raw_input('Give x y coords\n').strip()
        x, y = [int(i) for i in move.split() if i]
        x -= 1
        y -= 1
        mv = game.move(int(x), int(y))
        print(move)
        while mv == None:
            move = raw_input('Give x y coords').strip()
            x, y = [int(i) for i in move.split() if i]
            mv = game.move(int(x), int(y))
        if mv == 'bad':
            game.face = ':('
            game.draw_board()
            print('Game Over')
            sys.exit()


if __name__ == '__main__':
    main()
