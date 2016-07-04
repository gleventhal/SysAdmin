#!/usr/bin/python
from random import choice as c
from string import zfill
import sys, time, os

def exit(board,e=None):
    board.draw()
    if not e:
        sys.exit(-1)
    else:
        print "Knights Tour failed to complete!\n"
        raise(Exception(e))
        sys.exit(-1)

class Board(list):
    def __init__(self):
        self.board = [[ '00' for i in range(8)] for i in range(8) ]

    def draw(self):
        for square in self.board:
            print square

    def get(self,cor):
        return self.board[cor[0]][cor[1]]

    def set(self,cor,v):
        self.board[cor[0]][cor[1]] = zfill(str(v), 2)

def visited(board,cor):
    return(board.get(cor) != '00')


def knight_moves(board,cor):
    x = [ 1, 2, -1, -2,  1, 2, -2, -1 ]
    y = [ 2, 1,  2,  1, -2,-1, -1, -2 ]
    possible = []
    for i in range(8):
        dest = (cor[0] + x[i], cor[1] + y[i])
        if dest[0] in range(8) and dest[1] in range(8):
            if not visited(board,dest):
                possible.append(dest)
    return possible

def move(board,cor):
    possible_moves = knight_moves(board,cor)
    best_choice = (100, None)
    if possible_moves:
        for mv in possible_moves:
            next_square_choices = knight_moves(board,mv)
            if best_choice[0] > len(next_square_choices) > 0:
                best_choice = (len(next_square_choices),mv)
    if best_choice[0] == 100:
        board.draw()
        exit(board,"There were no moves available from the next square")
    else:
        return best_choice[1]
          
def main():
    b = Board()
    start_pos = (c(range(8)),c(range(8)))
    b.set(start_pos,1)
    last_move = start_pos
    i = 2
    while i < 64:
        next_possible = move(b,last_move)
        b.set(next_possible, i)
        i = i + 1
        last_move = next_possible
    b.set(knight_moves(b,last_move)[0],i)
    print "SUCCESS!"
    b.draw()
        
if __name__ == '__main__':
    main()            
