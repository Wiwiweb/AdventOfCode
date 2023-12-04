import re

r = r"Card ([\d ]+): ([\d ]+)\|([\d ]+)"

result = 0
card_values = {}
with open("2023/4-input.txt") as file:
    data = file.read().strip()
    lines = data.split('\n')

    for line in reversed(lines):
        matches = re.search(r, line)
        card_id = int(matches[1].strip())
        winning_numbers = set(re.split(r"  | ", matches[2].strip()))
        game_numbers = set(re.split(r"  | ", matches[3].strip()))
        # print(winning_numbers, game_numbers)
        win_number_count = len(game_numbers.intersection(winning_numbers))

        card_value = 1
        for i in range(card_id+1, card_id+1+win_number_count) :
            card_value += card_values[i]
        card_values[card_id] = card_value
        result += card_value

print(result)
