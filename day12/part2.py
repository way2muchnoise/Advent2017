import collections

f = open('input.txt', 'r')
lines = f.readlines()
f.close()


class Node:
    def __init__(self, name):
        self.name = name
        self.neighbours = []

    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)


raw_nodes_list = []
nodes = {}
for line in lines:
    (node_name, connections) = line.replace('\n', '').split(' <-> ')
    raw_nodes_list.append((node_name, connections))
    nodes[node_name] = Node(node_name)

for (node_name, connections) in raw_nodes_list:
    node = nodes[node_name]
    for connection in connections.split(', '):
        node.add_neighbour(nodes[connection])

groups = 0
while len(nodes) > 0:
    visited = set()
    visit_queue = collections.deque()
    visit_queue.append(nodes.values()[0])
    while len(visit_queue) > 0:
        current_node = visit_queue.popleft()
        for neighbour in current_node.neighbours:
            if neighbour.name not in visited and visit_queue.count(neighbour) == 0:
                visit_queue.append(neighbour)
        visited.add(current_node.name)
    groups += 1
    for node_name in visited:
        del nodes[node_name]
print groups
