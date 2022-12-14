import copy
from lib.grid import create_grid, get_item, print_grid_range, set_item
from lib.vector import Vector

with open("14-input.txt") as file:
    data = file.read().strip()
    lines = data.split('\n')

grid = create_grid(1000, 1000, '.')
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
            if point == seg_to:
                break
            point += diff
print_grid_range(grid, (0,0), (1000,1000))


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


print_grid_range(grid, (0,0), (1000,1000))
print(sand)
