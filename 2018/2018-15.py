from lib.grid import *;
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.finder.dijkstra import DijkstraFinder

with open("2018-15.txt") as file:
  data = file.read().strip()
  grid = data_to_grid(data)
  pathfinding_grid = replace_in_grid(grid, '.', 1)
  pathfinding_grid = replace_in_grid(pathfinding_grid, '#', 0)
  pathfinding_grid = replace_in_grid(pathfinding_grid, 'G', 0)
  pathfinding_grid = replace_in_grid(pathfinding_grid, 'E', 0)
  print_grid(grid)
  print()
  print_grid(pathfinding_grid)

  
grid = Grid(matrix=pathfinding_grid)
start = grid.node(5, 20)
end = grid.node(25, 15)
finder = DijkstraFinder(diagonal_movement=DiagonalMovement.never)
path, runs = finder.find_path(start, end, grid)
print('operations:', runs, 'path length:', len(path))
print(grid.grid_str(path=path, start=start, end=end))