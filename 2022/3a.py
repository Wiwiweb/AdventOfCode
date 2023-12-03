sum = 0
with open("3-input.txt") as file:
  lines = file.read().split('\n')
  for line in lines:
    midpoint = int(len(line)/2)
    first_half = set(line[:midpoint])
    second_half = set(line[midpoint:])
    common = first_half.intersection(second_half)
    (common,) = common
    if common.isupper():
      common = common.lower()
      sum += 26
    common_digit = ord(common) - 96
    sum += common_digit

print(sum)
