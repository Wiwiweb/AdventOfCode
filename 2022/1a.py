with open("1-input.txt") as file:
  max_calories = 0
  current_elf_calories = 0
  for line in file:
    if line == "\n":
      if current_elf_calories > max_calories:
        max_calories = current_elf_calories
      current_elf_calories = 0
    else:
      current_elf_calories += int(line)

print(max_calories)
