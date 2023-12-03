import regex as re

result = 0
with open("2-input.txt") as file:
    data = file.read().strip()
    lines = data.split('\n')
    for line in lines:
        game_id = int(re.findall(r"Game (\d+)", line)[0])
        game_color_power = 1
        for color in ["red", "green", "blue"]:
            color_nbs = re.findall(r"(\d+) " + color, line)
            color_nbs = [ int(x) for x in color_nbs ]
            game_color_max = max(color_nbs)
            # print(f"id: {game_id}, {color}: {color_nbs} ({game_color_max})")
            game_color_power = game_color_power * game_color_max
        result = result + game_color_power

print(result)
