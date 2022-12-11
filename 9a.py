def vector_add(v1, v2):
  return (v1[0] + v2[0], v1[1] + v2[1])

def vector_sub(v1, v2):
  return (v1[0] - v2[0], v1[1] - v2[1])

def is_neighbor(v1, v2):
  diff = vector_sub(v1, v2)
  return abs(diff[0]) <= 1 and abs(diff[1]) <= 1


visited = set()
with open("9-input.txt") as file:
    data = file.read().strip()
    lines = data.split('\n')
    head = (0, 0)
    tail = (0, 0)
    visited.add(tail)
    for line in lines:
      print(line)
      direction_letter, length = line.split(' ')
      match direction_letter:
        case 'L':
          direction = (-1, 0)
        case 'R':
          direction = (1, 0)
        case 'U':
          direction = (0, 1)
        case 'D':
          direction = (0, -1)
      for i in range(int(length)):
        head = vector_add(head, direction)
        print('head: ' + str(head))
        if not is_neighbor(head, tail):
          diff = vector_sub(head, tail)
          diff = list(diff)
          if diff[0] > 1:
            diff[0] = 1
          elif diff[0] < -1:
            diff[0] = -1
          if diff[1] > 1:
            diff[1] = 1
          elif diff[1] < -1:
            diff[1] = -1
          print('diff: ' + str(diff))
          tail = vector_add(tail, diff)
          visited.add(tail)
          print('tail: ' + str(tail))

print(len(visited))
        


