f = open('input.txt', 'r')
lines = f.readlines()
f.close()

firewalls = {}
last_depth = 0
for line in lines:
    (layer_depth, scan_range) = line.replace('\n', '').split(': ')
    firewalls[layer_depth] = int(scan_range)
    last_depth = int(layer_depth)

caught = True
delay = 500000
while caught:
    delay += 1
    caught = False
    for t in range(0, last_depth + 1):
        if str(t) in firewalls and (t + delay) % (2 * firewalls[str(t)] - 2) == 0:
            caught = True
            break
print delay
