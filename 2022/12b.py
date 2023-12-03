import math
from lib.grid import data_to_grid, four_neighbors_indexes, get_item, print_grid

def letter_to_height(letter):
    if letter == 'E':
      letter = 'z'
    if letter == 'S':
      letter = 'a'
    return ord(letter)

with open("12-input.txt") as file:
    data = file.read().strip()
    grid = data_to_grid(data)
    unvisited = set()
    distance = []
    start_pos = None
    end_nodes = []

    # init
    for x in range(len(grid)):
      distance.append([])
      for y in range(len(grid[0])):
        unvisited.add((x, y))
        if grid[x][y] == 'E':
          distance[x].append(0)
          current_node = (x, y)
        else:
          if grid[x][y] == 'a':
            end_nodes.append((x, y))
          distance[x].append(math.inf)


    while True:
      print(current_node)
      current_height = letter_to_height(get_item(grid, current_node))
      current_distance = get_item(distance, current_node)

      neighbor_indexes = four_neighbors_indexes(grid, current_node)
      for neighbor_node in neighbor_indexes:
        if neighbor_node in unvisited:
          neighbor_height = letter_to_height(get_item(grid, neighbor_node))
          if current_height -1 <= neighbor_height:
            x, y = neighbor_node
            distance[x][y] = min(distance[x][y], current_distance + 1)
      unvisited.remove(current_node)

      min_distance = math.inf
      current_node = None
      for x in range(len(distance)):
        for y in range(len(distance[0])):
          if (x, y) in unvisited and distance[x][y] < min_distance:
            min_distance = distance[x][y]
            current_node = (x, y)
      if current_node == None:
        break

min_distance = math.inf
final_node = None
for end_node in end_nodes:
  this_distance = get_item(distance, end_node)
  if this_distance < min_distance:
    min_distance = this_distance
    final_node = end_node


print_grid(distance)
print(end_node)
print(min_distance)
