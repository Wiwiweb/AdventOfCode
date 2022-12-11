import math
import string
import itertools
import more_itertools
import re
from anytree import Node, RenderTree

with open("7-input.txt") as file:
    data = file.read().strip()
    lines = data.split('\n')

    directory_tree_root = Node(r'/', size=0)
    current_directories = [directory_tree_root]
    for line in lines:
      if line == r"$ cd /":
        continue
      # print(line)
      parts = line.split(' ')
      if parts[0] == '$':
        if parts[1] == 'cd':
          if parts[2] == '..':
            current_directories.pop()
          else:
            if len(current_directories) > 0: 
              parent = current_directories[-1] 
            else:
              parent = directory_tree_root
            directory = Node(parts[2], parent=parent, size=0)
            current_directories.append(directory)
      elif parts[0] != 'dir':
        current_directory = current_directories[-1]
        processing_dir = current_directory
        while processing_dir:
          processing_dir.size += int(parts[0])
          processing_dir = processing_dir.parent

sum = 0
for pre, fill, node in RenderTree(directory_tree_root):
  print("%s%s (%i)" % (pre, node.name, node.size))
  if node.size <= 100000:
    sum += node.size
print(sum)

free_space = 70000000 - directory_tree_root.size
space_to_free = 30000000 - free_space

min_size = math.inf
for pre, fill, node in RenderTree(directory_tree_root):
  print("%s%s (%i)" % (pre, node.name, node.size))
  if node.size >= space_to_free:
    min_size = min(min_size, node.size)
print(min_size)