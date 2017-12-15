f = open('input.txt', 'r')
line = f.readline()
f.close()

suffix_sequence = [17, 31, 73, 47, 23]


def knot_hash(input_list, sequence):
    global skip_value, current_position
    for to_reverse in sequence:
        start = current_position
        end = current_position + to_reverse
        if end <= len(input_list):
            input_list[start:end] = reversed(input_list[start:end])
        else:
            to_reverse_list = input_list[start:]
            end = end % len(input_list)
            to_reverse_list.extend(input_list[:end])
            reversed_list = []
            reversed_list[0:] = reversed(to_reverse_list)
            input_list[start:] = reversed_list[:len(input_list[start:])]
            input_list[:end] = reversed_list[-len(input_list[:end]):]
        current_position += to_reverse + skip_value
        current_position %= len(input_list)
        skip_value += 1
    return input_list


used = 0
for row in range(0, 128):
    knotting_list = range(0, 256)
    skip_value = 0
    current_position = 0
    row_sequence = map(ord, line + '-' + str(row))
    row_sequence.extend(suffix_sequence)
    for x in range(0, 64):
        knotting_list = knot_hash(knotting_list, row_sequence)
    dense = ""
    for x in range(0, 256, 16):
        xored = knotting_list[x]
        for n in knotting_list[x + 1:x + 16]:
            xored ^= n
        hexed = hex(xored)[2:]
        if len(hexed) == 1:
            hexed = '0' + hexed
        dense += hexed
    binary = ''
    for char in dense:
        binary += bin(int(char, 16))[2:].zfill(4)
    used += binary.count('1')
print used
