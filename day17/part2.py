puzzle_input = 316

step = puzzle_input
position = 0
zero_index = 0
after_zero = -1
i = 1
while i <= 50000000:
    position = ((position + step) % i) + 1
    if position <= zero_index:  # insert before 0
        zero_index += 1
        print 'insert before', i
    elif position == zero_index + 1:  # insert right after 0
        after_zero = i
        print 'after zero', i
    i += 1
print after_zero
