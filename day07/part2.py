import re

import collections

f = open('input.txt', 'r')
lines = f.readlines()
f.close()

node_structure = re.compile(r'(.*) \((\d+)\)(?: -> (.*))?(?:\n|$)')


class Node:
    def __init__(self, name, weight, children):
        self.parent = None
        self.tower_weight = -1
        self.name = name
        self.weight = int(weight)
        self.children = []
        if children is not None:
            self.children.extend(children.split(', '))

    def set_parent(self, parent):
        self.parent = parent

    def set_tower_weight(self, weight):
        self.tower_weight = weight

    def is_balanced(self, nodes):
        if len(self.children) == 0:
            return True
        else:
            weights = set()
            for child in self.children:
                weights.add(nodes[child].tower_weight)
            if len(weights) == 1:
                return True
            else:
                return False

    def show_balance(self, nodes):
        for child in self.children:
            print child, nodes[child].weight, nodes[child].tower_weight


nodes = {}
for line in lines:
    match = node_structure.match(line)
    node = Node(match.group(1), match.group(2), match.group(3))
    nodes[node.name] = node
for node in nodes.values():
    for child in node.children:
        nodes[child].set_parent(node.name)

node_queue = collections.deque()
for node in nodes.values():
    if len(node.children) == 0:
        node_queue.append(node)

while len(node_queue) > 0:
    node = node_queue.popleft()
    if -1 in map(lambda x: nodes[x].tower_weight, node.children):
        node_queue.append(node)  # try node again later when children are resolved
        continue
    tower_weight = node.weight
    for child in node.children:
        tower_weight += nodes[child].tower_weight
    node.set_tower_weight(tower_weight)
    if not node.is_balanced(nodes):
        node.show_balance(nodes)
        break
    if node.parent is not None:
        parent = nodes[node.parent]
        if parent.tower_weight == -1 and node_queue.count(parent) == 0:
            node_queue.append(parent)
