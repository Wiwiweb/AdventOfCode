# from itertools import *
# from more_itertools import *
# from string import *

sum = 0
with open("4-input.txt") as file:
    lines = file.read().split('\n')
    for line in lines:
      pair = line.split(',')
      first = pair[0].split('-')
      second = pair[1].split('-')
      first = [int(first[0]), int(first[1])]
      second = [int(second[0]), int(second[1])]
      if first[0] <= second[0] and second[1] <= first[1]:
        sum += 1
      elif second[0] <= first[0] and first[1] <= second[1]:
        sum += 1


print(sum)
