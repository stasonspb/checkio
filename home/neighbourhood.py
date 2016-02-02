#!/usr/bin/python
import random
board = []
n = 1
def board_gen(n):
	for i in range(0,n):
		board.append([])
		for j in range(0,n):
			board[i].append(str(random.randint(0,1)))
	return board

def print_board(board):
    for row in board:
        print " ".join(row)

def check_neib(x, y):
	neib = 0
	for i in [y-1, y, y+1]:
		neib += board[i][x-1:x+2].count('1')
	print neib

while n < 3 or n > 10:
	n = input("vvedite razmer polyz(3-10): ")

x = input("vvedite koord x(0-%s): " % (n))
y = input("vvedite koord y(0-%s): " % (n))

board_gen(n)
board[y][x] = 'X'
print_board(board)
check_neib(x, y)