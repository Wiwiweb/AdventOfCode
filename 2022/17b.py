import math
from lib.grid import *
from lib.vector import Vector
import re
import os

pieces = []
with open("17-pieces.txt") as pieces_file:
    pieces_data = pieces_file.read().strip()
    pieces_strings = pieces_data.split('\n\n')
    for piece_string in pieces_strings:
        pieces.append(data_to_grid(piece_string))

moves = None
with open("17-input.txt") as file:
    data = file.read().strip()
    moves = list(data)

grid = create_grid(7, 1001, '.')

def can_fit(piece, position):
    for y in range(4):
        for x in range(4):
            piece_coord = Vector(x,y)
            if get_item(piece, piece_coord) == '#':
                grid_item = get_item(grid, position + piece_coord)
                if grid_item == '#' or grid_item == None:
                    return False
    return True



def apply_piece(piece, position):
    highest_piece_y = math.inf
    for y in range(4):
        for x in range(4):
            piece_coord = Vector(x,y)
            if get_item(piece, piece_coord) == '#':
                set_item(grid, position + piece_coord, '#')
                highest_piece_y = min(highest_piece_y, (position + piece_coord).y)
    return highest_piece_y

def move_grid_down(grid):
    grid = grid[:-100]
    for i in range(100):
        grid.insert(0, list('.......'))
    return grid

current_move = 0
i = 1
true_tower_height = 0
highest_block_y = len(grid) + 1
while i <= 1000000000000:
    if i % 1000000 == 0: print(i/1000000000000)
    next_piece = pieces[(i-1) % len(pieces)]
    position = Vector(2, highest_block_y-3-4)
    while True:
        next_move = moves[current_move % len(moves)]
        current_move += 1
        if next_move == '<':
            next_move = Vector(-1, 0)
        else:
            next_move = Vector(1, 0)
        if can_fit(next_piece, position + next_move):
            position += next_move

        next_move = Vector(0, 1)
        if can_fit(next_piece, position + next_move):
            position += next_move
        else:
            highest_piece_y = apply_piece(next_piece, position)
            if highest_piece_y < highest_block_y:
                true_tower_height += highest_block_y - highest_piece_y
                highest_block_y = min(highest_block_y, highest_piece_y)
                if highest_block_y < 100:
                    grid = move_grid_down(grid)
                    highest_block_y += 100
            break
    i += 1
    # os.system('cls')
    # print_grid_range(grid, (0, 9985), (6, 10000))
    # if i > 2: break


os.system('cls')
print_grid_range(grid, (0, 985), (6, 1000))
print(true_tower_height)