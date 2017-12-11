f = open('input.txt', 'r')
line = f.readline()
f.close()

index = 0
depth = 1
score = 0
is_garbage = False
while index < len(line):
    char = line[index]
    index += 1
    if char == '!':
        index += 1
        continue
    if is_garbage:
        if char == '>':
            is_garbage = False
    else:
        if char == '{':
            score += depth
            depth += 1
        elif char == '}':
            depth -= 1
        elif char == '<':
            is_garbage = True
print depth
print score
