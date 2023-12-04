import re

r = r"Card ([\d ]+): ([\d ]+)\|([\d ]+)"

result = 0
with open("2023/4-input.txt") as file:
    data = file.read().strip()
    lines = data.split('\n')

    for line in lines:
        matches = re.search(r, line)
        winning_numbers = set(re.split(r"  | ", matches[2].strip()))
        game_numbers = set(re.split(r"  | ", matches[3].strip()))
        print(winning_numbers, game_numbers)
        win_number_count = len(game_numbers.intersection(winning_numbers))
        if win_number_count > 0:
            result += pow(2, (win_number_count-1))

print(result)
