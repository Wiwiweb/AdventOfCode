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
    rope = [(0,0)] * 10
    visited.add((0,0))
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
        rope[0] = vector_add(rope[0], direction)
        for i in range(1, len(rope)):
          if not is_neighbor(rope[i-1], rope[i]):
            diff = vector_sub(rope[i-1], rope[i])
            diff = list(diff)
            if diff[0] > 1:
              diff[0] = 1
            elif diff[0] < -1:
              diff[0] = -1
            if diff[1] > 1:
              diff[1] = 1
            elif diff[1] < -1:
              diff[1] = -1
            rope[i] = vector_add(rope[i], diff)
            if i == len(rope) - 1:
              print(rope[i])
              visited.add(rope[i])


print(len(visited))
        


