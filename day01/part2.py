f = open('input.txt', 'r')
line = f.readline()
f.close()

total = 0
half = len(line) / 2
for x in range(0, len(line)):
    if line[x] == line[(x + half) % len(line)]:
        total += int(line[x])
print total
