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
  return grid[x][y]

def four_neighbors(grid, coords):
  x, y = coords
  neighbors = []
  if x-1 > 0:
    neighbors.append(grid[x-1][y])
  if x+1 < len(grid):
    neighbors.append(grid[x+1][y])
  if y-1 > 0:
    neighbors.append(grid[x][y-1])
  if y+1 < len(grid[1]):
    neighbors.append(grid[x][y+1])
  return neighbors

def four_neighbors_indexes(grid, coords):
  x, y = coords
  neighbors = []
  if x-1 >= 0:
    neighbors.append((x-1, y))
  if x+1 < len(grid):
    neighbors.append((x+1, y))
  if y-1 >= 0:
    neighbors.append((x, y-1))
  if y+1 < len(grid[1]):
    neighbors.append((x, y+1))
  return neighbors

def eight_neighbors(grid, coords):
  x, y = coords
  neighbors = []
  if x-1 >= 0:
    neighbors.append(grid[x-1][y])
    if y-1 >= 0:
      neighbors.append(grid[x-1][y-1])
    if y+1 < len(grid[1]):
      neighbors.append(grid[x-1][y+1])
  if x+1 < len(grid):
    neighbors.append(grid[x+1][y])
    if y-1 >= 0:
      neighbors.append(grid[x+1][y-1])
    if y+1 < len(grid[1]):
      neighbors.append(grid[x+1][y+1])
  if y-1 >= 0:
    neighbors.append(grid[x][y-1])
  if y+1 < len(grid[1]):
    neighbors.append(grid[x][y+1])
  return neighbors

def eight_neighbors_indexes(grid, coords):
  x, y = coords
  neighbors = []
  if x-1 > 0:
    neighbors.append((x-1, y))
    if y-1 > 0:
      neighbors.append((x-1, y-1))
    if y+1 < len(grid[1]):
      neighbors.append((x-1, y+1))
  if x+1 < len(grid):
    neighbors.append((x+1, y))
    if y-1 > 0:
      neighbors.append((x+1, y-1))
    if y+1 < len(grid[1]):
      neighbors.append((x+1, y+1))
  if y-1 > 0:
    neighbors.append((x, y-1))
  if y+1 < len(grid[1]):
    neighbors.append((x, y+1))
  return neighbors

def replace_in_grid(grid, char_from, char_to):
  new_grid = []
  for x in range(len(grid)):
    new_grid.append([])
    for y in range(len(grid[x])):
      if grid[x][y] == char_from:
        new_grid[x].append(char_to)
      else:
        new_grid[x].append(grid[x][y])
  return new_grid

def print_grid(grid):
  for x in range(480, 520):
    for y in range(len(grid[x])):
      print(grid[x][y], end='')
    print()

    # def print_grid(grid):
  # for x in range(len(grid)):
  #   for y in range(490, 510):
  #     print(grid[x][y], end='')
  #   print()


# with open("grid-input.txt") as file:
#   data = file.read().strip()
#   grid = data_to_grid(data)
#   coords = [30,31]
#   print(get_item(grid, coords))
#   print(four_neighbors_indexes(grid, coords))
#   print(four_neighbors(grid, coords))
#   print(eight_neighbors_indexes(grid, coords))
#   print(eight_neighbors(grid, coords))

