shape_score = {"X": 1, "Y": 2, "Z": 3}

with open("2-input.txt") as file:
  score = 0
  for line in file:
    first, second = line.split(' ')
    first = first.strip()
    second = second.strip()
    score += shape_score[second]

    if first == "A":
      if second == "X":
        score += 3
      elif second == "Y":
        score += 6
      elif second == "Z":
        score += 0

    elif first == "B":
      if second == "X":
        score += 0
      elif second == "Y":
        score += 3
      elif second == "Z":
        score += 6

    elif first == "C":
      if second == "X":
        score += 6
      elif second == "Y":
        score += 0
      elif second == "Z":
        score += 3

print(score)