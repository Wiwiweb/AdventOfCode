def compare_pair(l1, l2):
    for val1, val2 in zip(l1, l2):
        if isinstance(val1, int) and isinstance(val2, int):
            if val1 < val2:
                return True
            elif val1 > val2:
                return False
        else:
            if not isinstance(val1, list): val1 = [val1]
            if not isinstance(val2, list): val2 = [val2]
            correct = compare_pair(val1, val2)
            if correct != None:
                return correct
    if len(l1) < len(l2):
        return True
    if len(l1) > len(l2):
        return False
    return None

nb_before = 0
nb_between = 0
nb_after = 0
with open("13-input.txt") as file:
    data = file.read().strip()
    lines = data.split('\n')
    for line in lines:
        if line == "":
            continue
        line = eval(line)
        if compare_pair(line, [[2]]):
            nb_before += 1
        elif compare_pair(line, [[6]]):
            nb_between += 1
        else:
            nb_after += 1

print(nb_before, nb_between, nb_after)
print((nb_before + 1) * (nb_before + 1 + nb_between + 1))
