from lib.grid import data_to_grid

def score_from_direction(grid, x, y, x_dir, y_dir):
  tree_height = grid[x][y]
  check_pos = (x + x_dir, y + y_dir)
  score = 0
  while check_pos[0] >= 0 and check_pos[1] >= 0 \
    and check_pos[0] < len(grid) and check_pos[1] < len(grid[0]):
    score += 1
    check_tree_height = grid[check_pos[0]][check_pos[1]]
    if check_tree_height >= tree_height:
      break
    check_pos = (check_pos[0] + x_dir, check_pos[1] + y_dir)
  return score

max_score = 0
with open("8-input.txt") as file:
    data = file.read().strip()
    grid = data_to_grid(data)
    for x in range(len(grid)):
      for y in range(len(grid[0])):
        score = score_from_direction(grid, x, y, -1, 0) \
        * score_from_direction(grid, x, y, 1, 0) \
        * score_from_direction(grid, x, y, 0, -1) \
        * score_from_direction(grid, x, y, 0, 1)
        max_score = max(score, max_score)

print(max_score)
        