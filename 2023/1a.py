import regex as re

spelled_out_digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,}

def to_int(str):
  if str in spelled_out_digits:
    return spelled_out_digits[str]
  return int(str)

with open("1-input.txt") as file:
  sum = 0
  for line in file:
    digits = re.findall(r"\d|one|two|three|four|five|six|seven|eight|nine", line, overlapped=True)
    first = to_int(digits[0])
    last = to_int(digits[-1])
    # print(line, first, last)
    sum = sum + first * 10 + last

print(sum)

