#!/usr/bin/python
import random
from subprocess import call
from string import zfill

board = [ [ zfill(0,2) for i in range(8) ] for i in range(8) ]
all_moves = {}

def draw_board(b):
  call("clear")
  for i in b:
    print i

def movegen():
  for i in range(1,65):
    yield i

def move(x,y):
  can_move = [(1,2), (2,1), (-1,2), (1,-2), (-2,1), (2,-1), (-2,-1), (-1,-2)]
  possible_moves = []
  for mv in can_move:
    if x + mv[0] in range(8) and y + mv[1] in range(8):
      possible_moves.append(mv)
  if len(possible_moves) > 0:
    tup = random.choice(possible_moves)
    return (x + tup[0], y + tup[1])
  raise Exception("Ran out of options!")

start = (random.randint(0, 7),random.randint(0,7))
x = start[0]
y = start[1]
m = movegen()

while True:
  if board[x][y] == '00':
    next = m.next()
    board[x][y] = zfill(next, 2)
    draw_board(board)
    x,y = move(x,y)
    all_moves[next] = (x,y)
    print "\n\n"
    print all_moves.items()
    if next == 64:
      exit()
  else:
    x,y = move(x,y)
