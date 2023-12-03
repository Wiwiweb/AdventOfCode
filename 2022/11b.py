monkey_items = [
  [65, 78],
  [54, 78, 86, 79, 73, 64, 85, 88],
  [69, 97, 77, 88, 87],
  [99],
  [60, 57, 52],
  [91, 82, 85, 73, 84, 53],
  [88, 74, 68, 56],
  [54, 82, 72, 71, 53, 99, 67],
]

monkey_test = [
  lambda x: 2 if x % 5 == 0 else 3,
  lambda x: 4 if x % 11 == 0 else 7,
  lambda x: 5 if x % 2 == 0 else 3,
  lambda x: 1 if x % 13 == 0 else 5,
  lambda x: 7 if x % 7 == 0 else 6,
  lambda x: 4 if x % 3 == 0 else 1,
  lambda x: 0 if x % 17 == 0 else 2,
  lambda x: 6 if x % 19 == 0 else 0,
]

monkey_operation = [
  lambda x: x * 3,
  lambda x: x + 8,
  lambda x: x + 2,
  lambda x: x + 4,
  lambda x: x * 19,
  lambda x: x + 5,
  lambda x: x * x,
  lambda x: x + 1,
]

monkey_nb_inspections = [0] * 8
common_denominator = 5*11*2*13*7*3*17*19

for i in range(10000):
  print(i)
  for monkey_i in range(8):
    while len(monkey_items[monkey_i]) > 0:
      monkey_nb_inspections[monkey_i] += 1
      item = monkey_items[monkey_i][0]
      del monkey_items[monkey_i][0]
      item = monkey_operation[monkey_i](item)
      item = item % common_denominator
      next_monkey = monkey_test[monkey_i](item)
      monkey_items[next_monkey].append(item)

print(monkey_nb_inspections)
monkey_nb_inspections.sort()
print(monkey_nb_inspections)
