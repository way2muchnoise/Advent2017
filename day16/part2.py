import collections


f = open('input.txt', 'r')
line = f.readline()
f.close()

moves = line.split(',')

programs = collections.deque('abcdefghijklmnop')


def swap(x1, x2):
    global programs
    h = programs[x1]
    programs[x1] = programs[x2]
    programs[x2] = h


print ''.join(programs)
i = 0
while i < 10**9:
    for move in moves:
        if move[0] == 's':
            programs.rotate(int(move[1:]))
        elif move[0] == 'x':
            (x1, x2) = map(int, move[1:].split('/'))
            swap(x1, x2)
        elif move[0] == 'p':
            (p1, p2) = move[1:].split('/')
            current_programs = list(programs)
            x1 = current_programs.index(p1)
            x2 = current_programs.index(p2)
            swap(x1, x2)
    i += 1
    if ''.join(programs) == 'abcdefghijklmnop':
        print 'loops after', i
        i = 10**9 - (10**9 % i)
        print 'continuing from', i
print ''.join(programs)
