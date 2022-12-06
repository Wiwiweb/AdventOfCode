with open("6-input.txt") as file:
    data = file.read().strip()
    i = 14
    while True:
      characters = set(data[i-14:i])
      if len(characters) == 14:
        print(i)
        break
      i += 1
