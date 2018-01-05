f = open('input.txt', 'r')
lines = f.readlines()
f.close()


def move(curr, direction):
    curr = curr[:]
    if direction == 'left':
        curr[1] -= 1
    elif direction == 'right':
        curr[1] += 1
    elif direction == 'up':
        curr[0] -= 1
    elif direction == 'down':
        curr[0] += 1
    return curr


def get_symbol(location):
    global lines
    try:
        return lines[location[0]][location[1]]
    except IndexError:
        return ' '


def get_direction(curr, direction):
    curr_symbol = get_symbol(curr)
    if curr_symbol == '+':
        if direction == 'down' or direction == 'up':
            if get_symbol(move(curr, 'left')) != ' ':
                return 'left'
            else:
                return 'right'
        else:
            if get_symbol(move(curr, 'down')) != ' ':
                return 'down'
            else:
                return 'up'
    return direction


def follow_line(curr, direction):
    output = ''
    steps = 0
    while True:
        steps += 1
        direction = get_direction(curr, direction)
        curr = move(curr, direction)
        symbol = get_symbol(curr)
        if symbol.isalpha():
            output += symbol
        if symbol == ' ':
            break
    return output, steps


row = 0
col = 0
# go to start
while col < len(lines[row]) and lines[row][col] != '|':
    col += 1
print follow_line([row, col], 'down')


