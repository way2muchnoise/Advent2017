f = open('input.txt', 'r')
lines = f.readlines()
f.close()

jumps = map(int, lines)
curr_index = 0
jump_counter = 0
while len(jumps) > curr_index >= 0:
    jump = jumps[curr_index]
    if jump >= 3:
        jumps[curr_index] -= 1
    else:
        jumps[curr_index] += 1
    curr_index += jump
    jump_counter += 1
print jump_counter
