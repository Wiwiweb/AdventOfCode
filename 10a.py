x_at_cycle = [0, 1]
cycle = 1
with open("10-input.txt") as file:
    data = file.read().strip()
    lines = data.split('\n')
    for line in lines:
      if line == "noop":
        cycle += 1
        x_at_cycle.append(x_at_cycle[-1])
      else:
        _, val = line.split(' ')
        val = int(val)
        cycle += 1
        x_at_cycle.append(x_at_cycle[-1])
        cycle += 1
        x_at_cycle.append(x_at_cycle[-1] + val)

relevant_signals = [x_at_cycle[i] * i for i in range(20, 221, 40)]
# print(x_at_cycle)
# print(relevant_signals)
print(sum(relevant_signals))
