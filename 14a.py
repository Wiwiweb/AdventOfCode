import copy
import re
from grid import data_to_grid, four_neighbors_indexes, get_item, print_grid
# from more_itertools import windowed

def vector_add(v1, v2):
  return (v1[0] + v2[0], v1[1] + v2[1])

def vector_sub(v1, v2):
  return (v1[0] - v2[0], v1[1] - v2[1])

def vector_normalize(v):
    new_v = [v[0], v[1]]
    if new_v[0] > 1:
        new_v[0] = 1
    if new_v[0] < -1:
        new_v[0] = -1    
    if new_v[1] > 1:
        new_v[1] = 1
    if new_v[1] < -1:
        new_v[1] = -1
    return tuple(new_v)

with open("14-input-example.txt") as file:
    data = file.read().strip()
    lines = data.split('\n')
    grid = []
    grid_line = ['.'] * 1000
    highest_y = 0
    for i in range(1000):
        grid.append(copy.deepcopy(grid_line))
    for line in lines:
        elements = line.split(' -> ')
        for i in range(len(elements) - 1):
            seg_from, seg_to = elements[i], elements[i+1]
            print(seg_from, seg_to)
            seg_from = tuple(map(int, seg_from.split(',')))
            seg_to = tuple(map(int, seg_to.split(',')))
            diff = vector_sub(seg_to, seg_from)
            diff = vector_normalize(diff)
            point = seg_from
            while True:
                print(point)
                grid[point[0]][point[1]] = '#'
                if point == seg_to:
                    break
                point = vector_add(point, diff)
    print(highest_y)
    print_grid(grid)


    sand = 0
    origin = (500, 0)
    current_tile = origin
    while True:
        item = get_item(grid, current_tile)
        if item == None:
            break
        if item == 'o' or item == '#':
            diagonal_left_tile = get_item(grid, vector_add(current_tile, (-1, 0)))
            if diagonal_left_tile == 'o' or diagonal_left_tile == '#':

                diagonal_right_tile = get_item(grid, vector_add(current_tile, (1, 0)))
                if diagonal_right_tile == 'o' or diagonal_right_tile == '#':
                    grid[current_tile[0]][current_tile[1]-1] = 'o'
                    current_tile = origin
                    sand += 1
                    if current_tile == origin:
                        break
                else:
                    current_tile = vector_add(current_tile, (1, 1))
            else:
                current_tile = vector_add(current_tile, (-1, 1))

            
        else:
            current_tile = vector_add(current_tile, (0, 1))


print_grid(grid)
print(sand)
