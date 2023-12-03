with open("6-input.txt") as file:
    data = file.read().strip()
    i = 4
    while True:
      characters = set(data[i-4:i])
      if len(characters) == 4:
        print(i)
        break
      i += 1
