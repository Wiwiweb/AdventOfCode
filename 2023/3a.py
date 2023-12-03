from lib.grid import *
from lib.vector import Vector
import regex as re

grid_width = 0

def is_num_ok(grid, span):
    start_x = span[0] % grid_width
    end_x = (span[1]-1) % grid_width
    y = span[0] // grid_width
    print(start_x, end_x, y)
    for x in range(start_x, end_x+1):
        for neighbor in eight_neighbors_indexes(grid, Vector(x, y)):
            n = get_item(grid, neighbor)
            if n != None and n != '.' and not n.isalnum():
                return True
    return False

result = 0
with open("3-input.txt") as file:
    data = file.read().strip()
    grid = data_to_grid(data)
    grid_width = len(grid[0])

    data = data.replace('\n', '').replace('\r', '')
    numbers = re.finditer(r'\d+', data)
    for num in numbers:
        ok = is_num_ok(grid, num.span())
        # print(f"{num.group()}: {num.span()} {ok}")
        if ok:
            # print(num.group())
            result = result + int(num.group())

print(result)