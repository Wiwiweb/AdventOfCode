import more_itertools
import string

sum = 0
with open("3-input.txt") as file:
  lines = file.read().split('\n')
  for group in more_itertools.chunked(lines, 3):
    common = set(group[0]) & set(group[1]) & set(group[2])
    common = more_itertools.one(common)
    if common.isupper():
      common = common.lower()
      sum += 26
    common_digit = ord(common) - 96
    sum += common_digit

print(sum)
