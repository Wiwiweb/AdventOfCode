import copy
from lib.grid import create_grid, get_item, print_grid_range, replace_in_grid, set_item
from lib.vector import Vector

with open("14-input.txt") as file:
    data = file.read().strip()
    lines = data.split('\n')

grid = create_grid(1000, 1000, '.')
highest_y = 0
for line in lines:
    elements = line.split(' -> ')
    for i in range(len(elements) - 1):
        seg_from, seg_to = elements[i], elements[i+1]
        seg_from = Vector(map(int, seg_from.split(',')))
        seg_to = Vector(map(int, seg_to.split(',')))
        diff = seg_to - seg_from
        diff.dumb_normalize()
        point = seg_from
        while True:
            set_item(grid, point, '#')
            highest_y = max(highest_y, point.y)
            if point == seg_to:
                break
            point += diff
# print(highest_y)
for i in range(len(grid[0])):
    grid[highest_y+2][i] = '#' 
# print_grid_range(grid, (300,0), (700,highest_y+2))


sand = 0
origin = Vector(500, 0)
current_tile = origin
while True:
    item = get_item(grid, current_tile)
    if item == None:
        break
    if item == 'o' or item == '#':
        left_tile = get_item(grid, current_tile + Vector(-1, 0))
        if left_tile == 'o' or left_tile == '#':

            right_tile = get_item(grid, current_tile + Vector(1, 0))
            if right_tile == 'o' or right_tile == '#':
                set_item(grid, current_tile + Vector(0, -1), 'o')
                sand += 1
                if current_tile + Vector(0, -1) == origin:
                    break
                current_tile = origin
            else:
                current_tile += Vector(1, 1)
        else:
            current_tile += Vector(-1, 1)

        
    else:
        current_tile += Vector(0, 1)


grid = replace_in_grid(grid, '.', ' ')
# grid = replace_in_grid(grid, '#', '■')
grid = replace_in_grid(grid, 'o', '.')
print_grid_range(grid, (300,0), (700,highest_y+2))
# print(sand)
