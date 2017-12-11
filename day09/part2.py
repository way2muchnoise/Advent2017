f = open('input.txt', 'r')
line = f.readline()
f.close()

index = 0
garbage = 0
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
            garbage += 1
    else:
        if char == '<':
            is_garbage = True
print garbage
