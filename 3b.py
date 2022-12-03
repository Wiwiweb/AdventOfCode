sum = 0
with open("3-input.txt") as file:
  lines = file.read().split('\n')
  i = 0
  while i < len(lines):
    one = set(lines[i])
    two = set(lines[i+1])
    three = set(lines[i+2])
    common = one.intersection(two, three)
    (common,) = common
    if common.isupper():
      common = common.lower()
      sum += 26
    common_digit = ord(common) - 96
    sum += common_digit
    i += 3

print(sum)
