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

sum = 0
with open("13-input.txt") as file:
    data = file.read().strip()
    pairs = data.split('\n\n')
    i = 0
    for pair in pairs:
        i += 1
        l1, l2 = map(eval, pair.split('\n'))
        if compare_pair(l1, l2):
            print('correct:', i)
            sum += i


print(sum)
