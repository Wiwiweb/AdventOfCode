# from itertools import *
# from more_itertools import *
# from string import *

import re


bad_stacks = [
    ["G", "B", "D", "C", "P", "R"],
    ['G', 'V', 'H'],
    ['M', 'P', 'J', 'D', 'Q', 'S', 'N'],
    ['M', 'N', 'C', 'D', 'G', 'L', 'S', 'P'],
    ['S', 'L', 'F', 'P', 'C', 'N', 'B', 'J'],
    ['S', 'T', 'G', 'V', 'Z', 'D', 'B', 'Q'],
    ['Q', 'T', 'F', 'H', 'M', 'Z', 'B'],
    ['F', 'B', 'D', 'M', 'C'],
    ['G', 'Q', 'C', 'F'],
]

stacks = []

pattern = re.compile(r"""move (\d+) from (\d+) to (\d+)""")

for stack in bad_stacks:
    stacks.append(stack[::-1])

# print(stacks)

with open("5-input-2.txt") as file:
    data = file.read().strip()
    lines = data.split('\n')
    for line in lines:
        match = pattern.match(line)
        v_nb = int(match.group(1))
        v_from = int(match.group(2)) - 1
        v_to = int(match.group(3)) - 1
        # print(v_nb, v_from, v_to)
        for _ in range(v_nb):
            moving = stacks[v_from].pop()
            # print(stacks[v_from], moving, stacks[v_to])
            stacks[v_to].append(moving)

for stack in stacks:
    print(stack[-1])

