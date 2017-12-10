import re

f = open('input.txt', 'r')
lines = f.readlines()
f.close()

node_structure = re.compile(r'(.*) \((\d+)\)(?: -> (.*))?(?:\n|$)')


class Node:
    def __init__(self, name, weight, children):
        self.parent = None
        self.name = name
        self.weight = weight
        self.children = []
        if children is not None:
            self.children.extend(children.split(', '))

    def set_parent(self, parent):
        self.parent = parent


nodes = {}
for line in lines:
    match = node_structure.match(line)
    node = Node(match.group(1), match.group(2), match.group(3))
    nodes[node.name] = node
for node in nodes.values():
    for child in node.children:
        nodes[child].set_parent(node.name)
for node in nodes.values():
    if node.parent is None:
        print node.name
