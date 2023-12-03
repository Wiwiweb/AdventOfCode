from collections import namedtuple
from anytree import Node, RenderTree
import re




pattern = re.compile(r'Valve (..) has flow rate=(\d+); tunnels? leads? to valves? (.+)')

GraphNode = namedtuple('Node', ['flow', 'next_names', 'nexts'])



graph = None
previous_room = None
nodes = {}
with open("16-input-example.txt") as file:
    data = file.read().strip()
    lines = data.split('\n')
    for line in lines:
        match = pattern.match(line)
        valve_name, flow, leads_to = match.groups()
        flow = int(flow)
        leads_to = leads_to.split(', ')
        nodes[valve_name] = GraphNode(flow=flow, next_names=leads_to, nexts=[])

for node_name in nodes:
    node = nodes[node_name]
    for next_name in node.next_names:
        node.nexts.append(nodes[next_name])
    
decision_tree = 
print(nodes['AA'])
