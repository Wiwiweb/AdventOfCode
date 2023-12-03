from lib.grid import *
from lib.vector import Vector
import regex as re

grid_width = 0

def get_gear_coord(grid, span):
    start_x = span[0] % grid_width
    end_x = (span[1]-1) % grid_width
    y = span[0] // grid_width
    # print(start_x, end_x, y)
    for x in range(start_x, end_x+1):
        for neighbor in eight_neighbors_indexes(grid, Vector(x, y)):
            n = get_item(grid, neighbor)
            # print(n)
            if n == '*':
                return neighbor
    return None

gear_numbers = {}
result = 0
with open("3-input.txt") as file:
    data = file.read().strip()
    grid = data_to_grid(data)
    grid_width = len(grid[0])

    data = data.replace('\n', '').replace('\r', '')
    numbers = re.finditer(r'\d+', data)
    for num in numbers:
        coord = get_gear_coord(grid, num.span())
        # print(f"{num.group()}: {num.span()} {ok}")
        if coord:
            if coord not in gear_numbers:
                gear_numbers[coord] = []
            gear_numbers[coord].append(int(num.group()))


result = 0
for gear in gear_numbers:
    numbers = gear_numbers[gear]
    print(gear, numbers)
    if len(numbers) == 2:
        result = result + numbers[0] * numbers[1]

print(result)