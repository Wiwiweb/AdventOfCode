import re

stacks = [
    list('RPCDBG'),
    list('HVG'),
    list('NSQDJPM'),
    list('PSLGDCNM'),
    list('JBNCPFLS'),
    list('QBDZVGTS'),
    list('BZMHFTQ'),
    list('CMDBF'),
    list('FCQG'),
]

with open("5-input-2.txt") as file:
    data = file.read().strip()
    lines = data.split('\n')
    for line in lines:
        nb, from_stack, to_stack = map(int, re.findall('\d+', line))
        from_stack -= 1
        to_stack -= 1
        moving = stacks[from_stack][-nb:]
        stacks[from_stack] = stacks[from_stack][:-nb]
        stacks[to_stack] += moving


for stack in stacks:
    print(stack[-1], end='')
