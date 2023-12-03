import regex as re

max_colors = {
    "red": 12,
    "green": 13,
    "blue": 14,
}
result = 0
with open("2-input.txt") as file:
    data = file.read().strip()
    lines = data.split('\n')
    for line in lines:
        game_id = int(re.findall(r"Game (\d+)", line)[0])
        valid = True
        for color in ["red", "green", "blue"]:
            color_nbs = re.findall(r"(\d+) " + color, line)
            color_nbs = [ int(x) for x in color_nbs ]
            game_color_max = max(color_nbs)
            print(f"id: {game_id}, {color}: {color_nbs} ({game_color_max})")
            if game_color_max > max_colors[color]:
              print("BAD")
              valid = False
              break
        if valid:
            print("GOOD")
            result = result + game_id

print(result)
