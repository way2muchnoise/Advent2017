f = open('input.txt', 'r')
lines = f.readlines()
f.close()

firewalls = {}
last_depth = 0
for line in lines:
    (layer_depth, scan_range) = line.replace('\n', '').split(': ')
    firewalls[layer_depth] = int(scan_range)
    last_depth = int(layer_depth)

severity = 0
for t in range(0, last_depth+1):
    if str(t) in firewalls and t % (2*firewalls[str(t)] - 2) == 0:
        severity += t * firewalls[str(t)]
print severity
