f = open('input.txt', 'r')
line = f.readline()
f.close()

directions = line.split(',')

coord = {'x': 0, 'y': 0, 'z': 0}
max_distance = 0
for direction in directions:
    if direction == 'n':
        coord['x'] += 1
        coord['z'] -= 1
    elif direction == 'ne':
        coord['x'] += 1
        coord['y'] -= 1
    elif direction == 'se':
        coord['y'] -= 1
        coord['z'] += 1
    elif direction == 's':
        coord['x'] -= 1
        coord['z'] += 1
    elif direction == 'sw':
        coord['x'] -= 1
        coord['y'] += 1
    elif direction == 'nw':
        coord['y'] += 1
        coord['z'] -= 1
    max_distance = max(abs(coord['x']), abs(coord['y']), abs(coord['z']), max_distance)
print max_distance
