def print_pixel(cycle, x):
  char = '.'
  if (abs(((cycle-1) % 40) - x) <= 1):
    char = "#"
  print(char, end='')
  # print(cycle, ((cycle-1) % 40), x)
  if (cycle) % 40 == 0:
    print()

x_at_cycle = [0, 1]
cycle = 1
with open("10-input.txt") as file:
    data = file.read().strip()
    lines = data.split('\n')
    for line in lines:
      if line == "noop":
        print_pixel(cycle, x_at_cycle[-1])
        cycle += 1
        x_at_cycle.append(x_at_cycle[-1])
      else:
        _, val = line.split(' ')
        val = int(val)
        print_pixel(cycle, x_at_cycle[-1])
        cycle += 1
        x_at_cycle.append(x_at_cycle[-1])
        print_pixel(cycle, x_at_cycle[-1])
        cycle += 1
        x_at_cycle.append(x_at_cycle[-1] + val)

