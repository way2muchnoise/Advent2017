f = open('input.txt', 'r')
lines = f.readlines()
f.close()


class Sweeper:
    def __init__(self, depth, range):
        self.depth = depth
        self.range = range
        self.direction = 1
        self.position = 0

    def move(self):
        if self.position + self.direction > self.range - 1:
            self.direction = -1
        elif self.position + self.direction < 0:
            self.direction = 1
        self.position += self.direction


firewalls = {}
last_depth = 0
for line in lines:
    (layer_depth, scan_range) = line.replace('\n', '').split(': ')
    firewalls[layer_depth] = Sweeper(layer_depth, int(scan_range))
    last_depth = int(layer_depth)

severity = 0
for t in range(0, last_depth+1):
    if str(t) in firewalls and firewalls[str(t)].position == 0:
        severity += t * firewalls[str(t)].range
    for f in firewalls.values():
        f.move()
print severity
