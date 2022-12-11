from grid import data_to_grid

def visible_from_direction(grid, x, y, x_dir, y_dir):
  tree_height = grid[x][y]
  check_pos = (x + x_dir, y + y_dir)
  while check_pos[0] >= 0 and check_pos[1] >= 0 and check_pos[0] < len(grid) and check_pos[1] < len(grid[0]):
    check_tree_height = grid[check_pos[0]][check_pos[1]]
    if check_tree_height >= tree_height:
      return False
    check_pos = (check_pos[0] + x_dir, check_pos[1] + y_dir)
  print("visible: " + str(x_dir) + ", " + str(y_dir))
  return True

visible = 0
with open("8-input.txt") as file:
    data = file.read().strip()
    grid = data_to_grid(data)
    for x in range(len(grid)):
      for y in range(len(grid[0])):
        print(x,y)
        if visible_from_direction(grid, x, y, -1, 0) \
        or visible_from_direction(grid, x, y, 1, 0) \
        or visible_from_direction(grid, x, y, 0, -1) \
        or visible_from_direction(grid, x, y, 0, 1):
          visible += 1
print(visible)
        


