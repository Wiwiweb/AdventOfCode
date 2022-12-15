from lib.vector import Vector


def create_grid(x, y, item):
  return [[item for _ in range(x)] for _ in range(y)]

def data_to_grid(data):
  grid = []
  lines = data.split('\n')
  for line in lines:
    grid_line = list(line)
    grid.append(grid_line)
  return grid

def get_item(grid, coords):
  x, y = coords
  if x < 0 or x >= len(grid):
    return None
  if y < 0 or y >= len(grid[x]):
    return None
  return grid[y][x]

def set_item(grid, coords, item):
  x, y = coords
  if x < 0 or x >= len(grid):
    return
  if y < 0 or y >= len(grid[x]):
    return
  grid[y][x] = item

def four_neighbors(grid, coords):
  x, y = coords
  neighbors = []
  if x-1 > 0:
    neighbors.append(grid[y][x-1])
  if x+1 < len(grid):
    neighbors.append(grid[y][x+1])
  if y-1 > 0:
    neighbors.append(grid[y-1][x])
  if y+1 < len(grid[1]):
    neighbors.append(grid[y+1][x])
  return neighbors

def four_neighbors_indexes(grid, coords):
  x, y = coords
  neighbors = []
  if x-1 >= 0:
    neighbors.append(Vector(x-1, y))
  if x+1 < len(grid):
    neighbors.append(Vector(x+1, y))
  if y-1 >= 0:
    neighbors.append(Vector(x, y-1))
  if y+1 < len(grid[1]):
    neighbors.append(Vector(x, y+1))
  return neighbors

def eight_neighbors(grid, coords):
  x, y = coords
  neighbors = []
  if x-1 >= 0:
    neighbors.append(grid[y][x-1])
    if y-1 >= 0:
      neighbors.append(grid[y-1][x-1])
    if y+1 < len(grid[1]):
      neighbors.append(grid[y+1][x-1])
  if x+1 < len(grid):
    neighbors.append(grid[y][x+1])
    if y-1 >= 0:
      neighbors.append(grid[y-1][x+1])
    if y+1 < len(grid[1]):
      neighbors.append(grid[y+1][x+1])
  if y-1 >= 0:
    neighbors.append(grid[y-1][x])
  if y+1 < len(grid[1]):
    neighbors.append(grid[y+1][x])
  return neighbors

def eight_neighbors_indexes(grid, coords):
  x, y = coords
  neighbors = []
  if x-1 > 0:
    neighbors.append(Vector(x-1, y))
    if y-1 > 0:
      neighbors.append(Vector(x-1, y-1))
    if y+1 < len(grid[1]):
      neighbors.append(Vector(x-1, y+1))
  if x+1 < len(grid):
    neighbors.append(Vector(x+1, y))
    if y-1 > 0:
      neighbors.append(Vector(x+1, y-1))
    if y+1 < len(grid[1]):
      neighbors.append(Vector(x+1, y+1))
  if y-1 > 0:
    neighbors.append(Vector(x, y-1))
  if y+1 < len(grid[1]):
    neighbors.append(Vector(x, y+1))
  return neighbors

def replace_in_grid(grid, char_from, char_to):
  new_grid = []
  for y in range(len(grid)):
    new_grid.append([])
    for x in range(len(grid[y])):
      if grid[y][x] == char_from:
        new_grid[y].append(char_to)
      else:
        new_grid[y].append(grid[y][x])
  return new_grid

def print_grid(grid):
  for y in range(len(grid)):
    for x in range(len(grid[y])):
      print(grid[y][x], end='')
    print()

def print_grid_range(grid, top_left, bottom_right):
  for y in range(top_left[1], bottom_right[1]+1):
    for x in range(top_left[0], bottom_right[0]+1):
      print(grid[y][x], end='')
    print()


# with open("grid-input.txt") as file:
#   data = file.read().strip()
#   grid = data_to_grid(data)
#   coords = [30,31]
#   print(get_item(grid, coords))
#   print(four_neighbors_indexes(grid, coords))
#   print(four_neighbors(grid, coords))
#   print(eight_neighbors_indexes(grid, coords))
#   print(eight_neighbors(grid, coords))

